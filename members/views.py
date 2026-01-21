from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm

def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, "There was a problem with your info")
            return redirect('login')
    else:
        return render(request, "members/login.html", {})

def logout_user(request):
    logout(request)
    messages.success(request, "You were successfully logged out!")
    return redirect('home')

def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=user, password=password)
            login(request, user)
            messages.success(request, "You were successfully registered!")
            return redirect('home')
    else:
        form = UserCreationForm()

    return render(request, "members/register_user.html", {'form': form})
