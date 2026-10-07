from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import mixins
from rest_framework.generics import CreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView


# Create your views here.
class StudentAPIView(mixins.ListModelMixin,GenericAPIView):

    queryset = Student.objects.all()
    serializer_class = StudentSerializer

#mixins

    def get(self,request):
        return self.list(request)

#GenericAPIVIEW

    def post(self,request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk=None):
        std = self.get_object()
        serializer = self.get_serializer(std,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StudentCreateView(CreateAPIView):

#Generic API View
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class UpdateStudentView(RetrieveUpdateDestroyAPIView):

    queryset = Student.objects.all()
    serializer_class = StudentSerializer
