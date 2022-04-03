from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Department(models.Model):
    dept_name = models.CharField(max_length=150)


class Project(models.Model):
    proj_name = models.CharField(max_length=100)


class Employee(models.Model):
    name = models.CharField(max_length=150)
    job_title = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=35)
    salary = models.DecimalField(max_digits=6, decimal_places=3)
    dept_id = models.ForeignKey(Department, related_name="department", on_delete=models.CASCADE)
    proj_id = models.ForeignKey(Project, related_name="project", on_delete=models.CASCADE)
