from django.shortcuts import render,get_object_or_404
from rest_framework import generics,viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import employee
from .serializers import employeeSerializer

class employeeList(APIView):
    def get(self,request):
        value=employee.objects.all()
        serialize=employeeSerializer(value,many=True)
        return Response(serialize.data)

class employeesheet(viewsets.ModelViewSet):
        queryset=employee.objects.all()
        serializer_class=employeeSerializer