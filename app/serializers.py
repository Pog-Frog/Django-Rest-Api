from rest_framework import serializers
from .models import Employee , Project , Department

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'name', 'job_title', 'phone_no', 'salary', 'dept_id', 'proj_id']