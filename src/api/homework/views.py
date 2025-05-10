from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from homework.models import Homework
from .serializers import HomeworkSerializer



class HomeworkListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        if user.is_staff:
            homeworks = Homework.objects.all()
        elif user.role == 'teacher':
            homeworks = Homework.objects.filter(lesson__teacher=user)
        elif user.role == 'student':
            homeworks = Homework.objects.filter(lesson__group__students=user)
        else:
            return Response({"message": "You do not have permission"}, status=403)

        serializer = HomeworkSerializer(homeworks, many=True)
        return Response(serializer.data)

    def post(self, request):
        user = request.user
        if user.role != 'teacher' and not user.is_staff:
            return Response({"message": "Only teachers or admins can create homework"}, status=403)

        serializer = HomeworkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Homework created successfully"}, status=201)
        return Response(serializer.errors, status=400)


class HomeworkDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            homework = Homework.objects.get(pk=pk)
        except Homework.DoesNotExist:
            return Response({"message": "Homework not found"}, status=404)

        user = request.user
        if user.is_staff or \
                (user.role == 'teacher' and homework.lesson.teacher == user) or \
                (user.role == 'student' and user in homework.lesson.group.students.all()):
            serializer = HomeworkSerializer(homework)
            return Response(serializer.data)

        return Response({"message": "Permission denied"}, status=403)

    def put(self, request, pk):
        try:
            homework = Homework.objects.get(pk=pk)
        except Homework.DoesNotExist:
            return Response({"message": "Homework not found"}, status=404)

        user = request.user
        if not (user.is_staff or (user.role == 'teacher' and homework.lesson.teacher == user)):
            return Response({"message": "Only teachers or admins can update this homework"}, status=403)

        serializer = HomeworkSerializer(homework, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Homework updated successfully"})
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        try:
            homework = Homework.objects.get(pk=pk)
        except Homework.DoesNotExist:
            return Response({"message": "Homework not found"}, status=404)

        if not request.user.is_staff:
            return Response({"message": "Only admins can delete this homework"}, status=403)

        homework.delete()
        return Response({"message": "Homework deleted successfully"}, status=204)
