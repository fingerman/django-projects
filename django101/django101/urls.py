from django.contrib import admin
from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import path
from django.views.generic import ListView

from django101.views import index, UsersListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('2/', UsersListView.as_view()),

]



