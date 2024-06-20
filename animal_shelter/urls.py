from django.contrib import admin
from django.urls import path, include
from animals import views as animals_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('animals/', include('animals.urls')),
    path('employees/', animals_views.employee_list, name='employee_list'),
    path('feeds/', animals_views.feed_list, name='feed_list'),
    path('accounts/', animals_views.account_list, name='account_list'),
    path('', animals_views.index, name='index'),
]