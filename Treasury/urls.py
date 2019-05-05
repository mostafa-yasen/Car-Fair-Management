from django.urls import path
from . import views

urlpatterns = [
    path('', views.treasury, name='treasury'),
    # path('<int:car_id>/', views.car_details, name='car_details'),
    # path('expenses/', views.expenses, name='expenses'),
]