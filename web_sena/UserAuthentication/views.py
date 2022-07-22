from django.shortcuts import render

from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .decorators import authenticated_user


# Create your views here.
from .models import *
from .forms import RegisterForm


@authenticated_user
def registerView(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            messages.success(request, 'Usuario ' +
                             username + ' registrado exitosamente.')
            return redirect('login')
    context = {'form': form}
    return render(request, 'RegisterTemplate.html', context)


@authenticated_user
def loginView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(
                request, 'El nombre de usuario o contraseña son incorrectos.')
    context = {}
    return render(request, 'LoginTemplate.html', context)


def logoutRequest(request):
    logout(request)
    return redirect('login')
