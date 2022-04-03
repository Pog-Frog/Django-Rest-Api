from django.urls import path, include
from .views import EmployeeViewSet, DepartmentViewSet, ProjectViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('employees', EmployeeViewSet)
router.register('departments', DepartmentViewSet)
router.register('projects', ProjectViewSet)
urlpatterns = [
    path('', include(router.urls))
]
