from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies/', views.movies),
    path('movies/<int:id>', views.detail),
    path('', views.home),
    path('movies/add', views.add),
    path('movies/delete/<int:id>', views.delete),
]
