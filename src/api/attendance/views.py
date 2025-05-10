from rest_framework.views import APIView
from rest_framework.response import Response
from attendance.models import Attendance
from .serializers import AttendanceSerializer
from api.permissions import  IsAdmin,IsStudent,IsTeacher
from rest_framework.permissions import IsAuthenticated
from rest_framework import status



class AttendanceStudent(APIView):
    permission_classes = [IsAuthenticated]


    def get(self,request):
        if request.user.role == 'student':
            attendance = Attendance.objects.filter(student=request.user)
            serializer = AttendanceSerializer(attendance,many=True)
            return Response(serializer.data)
        return Response({"message":"You are not a student"})


class AttendanceTeacher(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        if request.user.role == 'teacher':
            attendance = Attendance.objects.filter(lesson__teacher=request.user)
            serializer = AttendanceSerializer(attendance)
            return Response(serializer.data)
        return Response({"message":"You are not a teacher"})


class AttendanceTeacherDetail(APIView):
    permission_classes = [IsAuthenticated]
    def put(self,request,pk):
        if request.user.role == 'teacher':
            attendance = Attendance.objects.get(lesson__teacher=request.user,pk=pk)
            serializer = AttendanceSerializer(instance=attendance,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"message":"Attendance updated successfully"})
            return Response(serializer.errors)
        return Response({"message":"You are not a teacher"})



class AdminAttendance(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):
        if request.user.is_staff:
            attendance = Attendance.objects.all()
            serializer = AttendanceSerializer(attendance)
            return Response(serializer.data)
        return Response({"message":"You are not an admin"})


    def post(self,request):
        if request.user.is_staff:
            serializer = AttendanceSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"message":"Attendance created successfully"})
            return Response(serializer.errors)
        return Response({"message":"You are not an admin"})



class AdminAttendanceDetail(APIView):
    permission_classes = [IsAuthenticated]

    def put(self,request,pk):
        if request.user.is_staff:
            attendance = Attendance.objects.get(pk=pk)
            serializer = AttendanceSerializer(instance=attendance,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"message":"Attendance updated successfully"})
            return Response(serializer.errors)
        return Response({"message":"You are not an admin"})








