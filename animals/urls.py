from django.urls import path
from . import views

urlpatterns = [
    path('', views.animal_list, name='animal_list'),
    path('<int:pk>/', views.animal_detail, name='animal_detail'),
    path('new/', views.animal_create, name='animal_create'),
    path('<int:pk>/edit/', views.animal_update, name='animal_update'),
    path('<int:pk>/delete/', views.animal_delete, name='animal_delete'),
]