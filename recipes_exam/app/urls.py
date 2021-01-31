from django.urls import path

from app.views import index, create, edit, delete, details

urlpatterns = [
    path('', index, name='home page'),
    path('create/', create, name='create recipe page'),
    path('edit/<int:pk>/', edit, name='edit recipe page'),
    path('delete/<int:pk>/', delete, name='delete recipe page'),
    path('details/<int:pk>/', details, name='details recipe page'),
]