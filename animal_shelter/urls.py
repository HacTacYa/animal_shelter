from django.contrib import admin
from django.urls import path, include
from animals import views as animals_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('animals/', include('animals.urls')),
    path('', animals_views.index, name='index'),
]