from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:car_id>/', views.details, name='details'),
]