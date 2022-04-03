from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from app.models import Employee, Department, Project
from rest_framework import viewsets
from .serializers import *


# Create your views here.

class EmployeeViewSet(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()


class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()


class DepartmentViewSet(viewsets.ModelViewSet):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()
