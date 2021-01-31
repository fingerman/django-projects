from django.shortcuts import render, redirect

from todo_app.forms import TodoForm
from todo_app.models import Todo


def index(req):
    context = {
        'todos': Todo.objects.all(),
        'todo_form': TodoForm(),
    }

    return render(req, 'todo_app/index.html', context=context)


def create(request):
    if request.method == 'GET':
        context = {
            'todo_form': TodoForm(),
        }
        return render(request, 'todo_app/create.html', context)
    else:
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = Todo(
                title=form.cleaned_data['title'],
                description=form.cleaned_data['description'],
                is_done=False)
            todo.save()
            return redirect('index')


