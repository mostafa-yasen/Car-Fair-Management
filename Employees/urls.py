from django.urls import path
from . import views

urlpatterns = [
    path('', views.employees, name='employees'),
    path('<int:employee_id>/', views.emp_details, name='emp_details'),
]