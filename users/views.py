from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, ProfileCreateForm, AddressUpdateForm, CardUpdateForm
from store.models import Book
from .models import Profile


# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
   
        if form.is_valid():
            form.save()
            messages.success(request, f'Cuenta creada exitosamente. Ahora puedes iniciar sesión')
            return redirect('login')
    else:
        form = UserRegisterForm()
       
    
    context = {
        'form': form,
    }
    return render(request, 'users/register.html', context)



@login_required
def profile(request):
    return render(request, 'users/user-profile.html')

@login_required
def profileInfo(request):
    if request.method == 'POST':
        uForm = UserUpdateForm(request.POST, instance=request.user)
        pForm = ProfileUpdateForm(request.POST, instance = request.user.profile)

        if uForm.is_valid() and pForm.is_valid():
            uForm.save()
            pForm.save()
            messages.success(request, f'Datos actualizados exitosamente')
            return redirect('user-profile')

    else:
        uForm = UserUpdateForm(instance=request.user)
        pForm = ProfileUpdateForm(instance = request.user.profile)
    context = {
        'uForm': uForm,
        'pForm': pForm
    }

    return render(request, 'users/user-profile-info.html', context)

@login_required
def addressInfo(request):
    if request.method == 'POST':
        #uForm = UserUpdateForm(request.POST, instance=request.user)
        aForm = AddressUpdateForm(request.POST, instance = request.user.profile)

        if aForm.is_valid():
            aForm.save()
            messages.success(request, f'Datos actualizados exitosamente')
            return redirect('user-profile')

    else:
        aForm = AddressUpdateForm(instance = request.user.profile)

    context = {
        'aForm': aForm,
    }

    return render(request, 'users/user-profile-address.html', context)

@login_required
def cardInfo(request):
    if request.method == 'POST':
        #uForm = UserUpdateForm(request.POST, instance=request.user)
        cForm = CardUpdateForm(request.POST, instance = request.user.profile)

        if cForm.is_valid():
            cForm.save()
            messages.success(request, f'Datos actualizados exitosamente')
            return redirect('user-profile')

    else:
        cForm = CardUpdateForm(instance = request.user.profile)

    context = {
        'cForm': cForm,
    }

    return render(request, 'users/user-profile-card.html', context)

#View for books from user
def profile_book_list(request):
    currentlyLoggedUser = request.user
    userProfile = Profile.objects.get(user=currentlyLoggedUser.id)
    books = Book.objects.filter(publishedBy= userProfile.user).order_by('-datePosted')

    context = {
        'books':books
    }

    return render(request, 'users/user-profile-books.html', context)
