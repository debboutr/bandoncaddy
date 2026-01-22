from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import LoopForm, PersonForm
from .models import Course, Group

def home(request):
   return render(request, "collect/home.html", {})


def detail(request):
    ...

@login_required
def add_work(request):
    courses = Course.objects.all()
    if request.method == "POST":
        form = LoopForm(data=request.POST, user=request.user)
        form.instance.author = request.user
        if form.is_valid():
            form.save()
            messages.success(request, "Loop data added successfully!")
            return redirect('home')

    else:
        form = LoopForm(user=request.user)
    return render(request, "collect/add_work.html", {
        'form': form,
        'courses': courses
        })

@login_required
def add_person(request):
    if request.method == "POST":
        form = PersonForm(request.POST)
        instance = form.save(commit=False)
        if not hasattr(instance, "group"):
            group = Group.objects.create(name=instance.first_name, author=request.user)
            instance.group = group
        if form.is_valid():
            form.save()
            messages.success(request, "Player added successfully!")
            return redirect('home')

    else:
        form = PersonForm()
    return render(request, "collect/add_person.html", {'form': form})
