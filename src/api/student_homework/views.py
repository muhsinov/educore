from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from homework.models import StudentHomework
from .serializers import StudentHomeworkSerializer




class StudentHomeworkListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        if user.is_staff:
            homeworks = StudentHomework.objects.all()
        elif user.role == 'teacher':
            homeworks = StudentHomework.objects.filter(homework__lesson__teacher=user)
        elif user.role == 'student':
            homeworks = StudentHomework.objects.filter(student=user)
        else:
            return Response({"message": "You do not have permission"}, status=403)

        serializer = StudentHomeworkSerializer(homeworks, many=True)
        return Response(serializer.data)

    def post(self, request):
        user = request.user
        if user.role != 'student':
            return Response({"message": "Only students can submit homework"}, status=403)

        serializer = StudentHomeworkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Homework submitted successfully"}, status=201)
        return Response(serializer.errors, status=400)


class StudentHomeworkDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return StudentHomework.objects.get(pk=pk)
        except StudentHomework.DoesNotExist:
            return None

    def get(self, request, pk):
        student_homework = self.get_object(pk)
        if not student_homework:
            return Response({"message": "Homework not found"}, status=404)

        user = request.user
        if user.is_staff or \
           (user.role == 'teacher' and student_homework.homework.lesson.teacher == user) or \
           (user.role == 'student' and student_homework.student == user):
            serializer = StudentHomeworkSerializer(student_homework)
            return Response(serializer.data)
        return Response({"message": "Permission denied"}, status=403)

    def put(self, request, pk):
        student_homework = self.get_object(pk)
        if not student_homework:
            return Response({"message": "Homework not found"}, status=404)

        user = request.user
        if user.is_staff or (user.role == 'teacher' and student_homework.homework.lesson.teacher == user):
            serializer = StudentHomeworkSerializer(student_homework, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "Homework updated successfully"})
            return Response(serializer.errors, status=400)
        return Response({"message": "Only teachers or admins can update this homework"}, status=403)

    def delete(self, request, pk):
        student_homework = self.get_object(pk)
        if not student_homework:
            return Response({"message": "Homework not found"}, status=404)

        if not request.user.is_staff:
            return Response({"message": "Only admins can delete this homework"}, status=403)

        student_homework.delete()
        return Response({"message": "Homework deleted successfully"}, status=204)
