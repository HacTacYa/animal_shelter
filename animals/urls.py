from django.urls import path
from . import views

urlpatterns = [
    path('', views.animal_list, name='animal_list'),  # List all animals
    path('add/', views.animal_add, name='animal_add'),
    path('animal/<int:pk>/', views.animal_detail, name='animal_detail'),  # Detail view of a single animal
    path('animal/new/', views.animal_create, name='animal_create'),  # Create a new animal
    path('animal/<int:pk>/edit/', views.animal_update, name='animal_update'),  # Update an existing animal
    path('animal/<int:pk>/delete/', views.animal_delete, name='animal_delete'),  # Delete an animal
]
