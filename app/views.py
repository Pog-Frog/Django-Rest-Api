from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from app.models import Employee, Department, Project
from rest_framework import viewsets
from .serializers import *


# Create your views here.

class EmployeeViewSet(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()

def get_all_employees(request):
    emp = list(Project.objects.values())
    print(emp)
    return JsonResponse(emp, safe=False)


def get_employee(request):
    return None
