from django.shortcuts import render, redirect

# Create your views here.
from core.clean_up import clean_up_files
from pets.forms.comment_form import CommentForm
from pets.forms.pets_form import PetForm
from pets.models import Pet, Comment, Like


def list_pets(request):
    context = {
        'pets': Pet.objects.all(),

    }

    return render(request, 'pet_list.html', context)


def details_or_comment_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'pet': pet,
            'form': CommentForm(),
        }

        return render(request, 'pet_detail.html', context)
    else:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(text=form.cleaned_data['text'])
            comment.pet = pet
            comment.save()
            return redirect('pet details or comment', pk)
        context = {
            'pet': pet,
            'form': form,
        }

        return render(request, 'pet_detail.html', context)


def like_pet(request, pk):
    # already_liked = Likes.objects.first(user_id=user.id, pk=pk)
    # if already_liked :
    #     return
    pet = Pet.objects.get(pk=pk)
    like = Like(test=str(pk))
    like.pet = pet
    like.save()
    return redirect('pet details or comment', pk)





def persist_pet(request, pet, template_name):
    if request.method == 'GET':
        form = PetForm(instance=pet)

        context = {
            'form': form,
            'pet': pet,
        }

        return render(request, f'{template_name}.html', context)
    else:
        old_image = pet.image
        form = PetForm(
            request.POST,
            request.FILES,
            instance=pet
        )
        if form.is_valid():
            if old_image:
                clean_up_files(old_image.path)
            form.save()
            Like.objects.filter(pet_id=pet.id) \
                .delete()
            return redirect('pet details or comment', pet.pk)

        context = {
            'form': form,
            'pet': pet,
        }

        return render(request, f'{template_name}.html', context)


def create_pet(request):
    pet = Pet()
    return persist_pet(request, pet, 'pet_create')


def edit_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    return persist_pet(request, pet, 'pet_edit')


def delete_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'pet': pet,
        }

        return render(request, 'pet_delete.html', context)
    else:
        pet.delete()
        return redirect('list pets')


def like_pet(request, pk):
    # already_liked = Likes.objects.first(user_id=user.id, pk=pk)
    # if already_liked :
    #     return
    pet = Pet.objects.get(pk=pk)
    like = Like(test=str(pk))
    like.pet = pet
    like.save()
    return redirect('pet details or comment', pk)
