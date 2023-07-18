from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, get_user_model, authenticate, logout
from django.http import *

from arad.views import *
from .forms import *
# Create your views here.
def login_view(request):
    if request.user.is_authenticated:
        return redirect('/')
    loginform = LoginForm(request.POST or None)
    if loginform.is_valid():
        print(loginform.cleaned_data)
        user = authenticate(request, username=loginform.cleaned_data['username'], password=loginform.cleaned_data['password'])
        if user:
            login(request, user)
            return redirect('/')
    context = {
        'loginform': loginform
    }
    return render(request, 'account/login.html', context)


def register_view(request):
    if request.user.is_authenticated:
        return redirect('/')
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data['username']
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        User.objects.create_user(username=username, email=email, password=password)
        return redirect('/login')
    context = {
        'rform':form
    }
    return render(request, 'account/register.html', context)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse(home_view))

