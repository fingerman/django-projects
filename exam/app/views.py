from django.shortcuts import render, redirect

from app.forms.animals import AnimalForm
from app.models import Animal


def index(request):
    if Animal.objects.exists():
        context = {
            'animals': Animal.objects.all(),
        }

        return render(request, 'home_with_sick_and_cured.html', context)
    else:
        return render(request, 'home_with_no_animals.html')


def persist(request, animal, template_name):
    if request.method == 'GET':
        context = {
            'form': AnimalForm(instance=animal),
        }

        return render(request, f'{template_name}.html', context)
    else:
        form = AnimalForm(request.POST, instance=animal)

        if form.is_valid():
            form.save()
            return redirect('home page')

        context = {
            'form': form,
        }

        return render(request, f'{template_name}.html', context)


def create(request):
    return persist(request, Animal(), 'create')


def edit(request, pk):
    return persist(request, Animal.objects.get(pk=pk), 'edit')


def delete(request, pk):
    animal = Animal.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'animal': animal,
        }

        return render(request, 'delete.html', context)
    else:
        animal.delete()
        return redirect('home page')


def details(request, pk):
    context = {
        'animal': Animal.objects.get(pk=pk),
    }

    return render(request, 'details.html', context)


def cure(request, pk):
    animal = Animal.objects.get(pk=pk)
    if animal.is_cured == False:
        animal.is_cured = True
        return redirect('home page')
    else:
        animal.delete()
        return redirect('home page')