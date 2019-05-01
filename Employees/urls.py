from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:employee_id>/', views.details, name='details'),
]