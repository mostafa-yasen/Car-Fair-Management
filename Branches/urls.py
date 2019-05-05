from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('branches/', views.index, name='index'),
    path('branches/<int:branch_id>/', views.details, name='details'),
]