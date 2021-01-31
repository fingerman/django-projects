from django.urls import path

from app.views import index, create, edit, delete, details, cure

urlpatterns = [
    path('', index, name='home page'),
    path('create/', create, name='add animal page'),
    path('edit/<int:pk>/', edit, name='edit animal page'),
    path('delete/<int:pk>/', delete, name='delete animal page'),
    path('details/<int:pk>/', details, name='details animal page'),
    path('cure/<int:pk>/', cure, name='cure animal'),
]