from django.shortcuts import render
from rest_framework.views import APIView
from demo1.serializer import StudentSerializer
from rest_framework.response import Response
from demo1.models import Student
from rest_framework import status

# Create your views here.


class DeployView(APIView):
    def get(self,request):
        data = Student.objects.all()
        serializer = StudentSerializer(data,many=True)
        content = {'Message': 'Data successfully retrieved'}
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self,request):
        datas = request.data
        serializer = StudentSerializer(data=datas)
        if serializer.is_valid():
            serializer.save()
        return Response({'msg':'Data Successfully saved!!!'},status=status.HTTP_201_CREATED)
    

