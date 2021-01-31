from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import ListView


def index(request):
    title = 'Page One'
    users = User.objects.all()
    context = {
        'users': users,
        'title': title,
    }

    return render(request, 'index.html', context)


class UsersListView(ListView):
    model = User
    template_name = 'index2.html'