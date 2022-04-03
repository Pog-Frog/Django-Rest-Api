from django.urls import path, include
from . import views
from .views import EmployeeViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('employees', EmployeeViewSet )
urlpatterns = [
    path('', include(router.urls))
]