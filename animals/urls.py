from django.urls import path
from . import views

urlpatterns = [
    path('', views.animal_list, name='animal_list'),  # Список всех животных
    path('add/', views.animal_add, name='animal_add'), # Добавить информацию о животном
    path('animal/<int:pk>/', views.animal_detail, name='animal_detail'),  # Просмотр информации об одном животном
    path('animal/<int:pk>/edit/', views.animal_update, name='animal_update'),  # Обновить информацию о животном
    path('animal/new/', views.animal_create, name='animal_create'),    
    path('animal/<int:pk>/delete/', views.animal_delete, name='animal_delete'),  # Удалить информацию о животном
    
    path('', views.employee_list, name='employee_list'),
    path('<int:pk>/', views.employee_detail, name='employee_detail'),
    path('employees/add/', views.employee_create, name='employee_create'),
    path('employees/<int:pk>/edit/', views.employee_update, name='employee_update'),
    path('employees/<int:pk>/delete/', views.employee_delete, name='employee_delete'),
    
    path('', views.feed_list, name='feed_list'),
    path('feed/<int:pk>/', views.feed_detail, name='feed_detail'),
    path('feed/add/', views.feed_create, name='feed_create'),
    path('feed/<int:pk>/edit/', views.feed_update, name='feed_update'),
    path('feed/<int:pk>/delete/', views.feed_delete, name='feed_delete'),
    
    path('accounts/', views.account_list, name='account_list'),
    path('account/<int:pk>/', views.account_detail, name='account_detail'),
    path('accounts/create/', views.account_create, name='account_create'),
    path('account/<int:pk>/update/', views.account_update, name='account_update'),
    path('account/<int:pk>/delete/', views.account_delete, name='account_delete'),
    path('account/<int:pk>/donation/add/', views.account_donation_create, name='account_donation_create'),
    path('account/<int:account_pk>/donation/<int:donation_pk>/delete/', views.account_donation_delete, name='account_donation_delete'),
]
