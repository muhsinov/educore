from rest_framework.views import APIView
from rest_framework.response import Response
from address.models import Address
from .serializers import AddressSerializer
from api.permissions import  IsAdmin,IsStudent,IsTeacher
from rest_framework.permissions import IsAuthenticated
from rest_framework import status


class AddressStudentDetail(APIView):
    permission_classes = [IsAuthenticated, IsStudent]

    def get(self, request):
        address = request.user.address
        if address:
            serializer = AddressSerializer(address)
            return Response(serializer.data)
        return Response({"message": "You have no address"})

    def put(self, request):
        address = request.user.address
        if request.user.role == 'student':
            if address:
                serializer = AddressSerializer(instance=address, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response({"message": "Address updated successfully"})
                return Response(serializer.errors)
            return Response({"message": "You have no address"})
        return Response({"message": "You are not a student"})

class AddressteacherApiView(APIView):
    def get(self,request):
        address = request.user.address
        if request.user.role == 'teacher':
            if address:
                serializer = AddressSerializer(address)
                return Response(serializer.data)

        return Response({"message":"You are not a teacher"})

    def put(self,request):
        address = request.user.address
        if request.user.role == 'teacher':
            if address:
                serializer = AddressSerializer(address,data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response({"message":"Address updated successfully"})
                return Response(serializer.errors)
            return Response({"message":"You have no address"})
        return Response({"message":"You are not a teacher"})



class allAddressApiview(APIView):
    def get(self,request):
        if request.user.is_staff:
            address = Address.objects.all()
            serializer = AddressSerializer(address, many=True)
            return Response(serializer.data)
        return Response({"message":"You are not an admin"})

    def post(self,request):
        if request.user.is_staff:
            serializer = AddressSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"message":"Address created successfully"})
            return Response(serializer.errors)
        return Response({"message":"You are not an admin or a teacher"})


class AddressDetailAdmin(APIView):
    def put(self,request,pk):
        if request.user.is_staff:
            address = Address.objects.get(pk=pk)
            serializer = AddressSerializer(address,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"message":"Address updated successfully"})
            return Response(serializer.errors)
        return Response({"message":"You are not an admin"})
