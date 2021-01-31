from django.shortcuts import render, redirect

# Create your views here.
from app.forms.recipes import RecipeForm
from app.models import Recipe


# def index(request):
#     if Recipe.objects.exists():
#         recipes = Recipe.objects.all(),
#
#         context = {
#             'recipes': recipes,
#         }
#
#         return render(request, 'index.html', context)
#     else:
#         return render(request, 'index_none.html')


def index(request):
    if Recipe.objects.exists():
        context = {
            'recipes': Recipe.objects.all(),
        }

        return render(request, 'index.html', context)
    else:
        return render(request, 'index_none.html')


def persist(request, recipe, template_name):
    if request.method == 'GET':
        context = {
            'form': RecipeForm(instance=recipe),
        }

        return render(request, f'{template_name}.html', context)
    else:
        form = RecipeForm(request.POST, instance=recipe)

        if form.is_valid():
            form.save()
            return redirect('home page')

        context = {
            'form': form,
        }

        return render(request, f'{template_name}.html', context)


def create(request):
    return persist(request, Recipe(), 'create')


def edit(request, pk):
    return persist(request, Recipe.objects.get(pk=pk), 'edit')


def delete(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'recipe': recipe,
        }

        return render(request, 'delete.html', context)
    else:
        recipe.delete()
        return redirect('home page')


def details(request, pk):
    context = {
        'recipe': Recipe.objects.get(pk=pk),
    }

    return render(request, 'details.html', context)
