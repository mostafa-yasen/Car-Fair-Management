from django.urls import path
from . import views

urlpatterns = [
    path('', views.clients, name='clients'),
    path('<int:client_id>/', views.details, name='details'),
]