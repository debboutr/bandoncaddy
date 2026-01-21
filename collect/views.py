from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import LoopForm, PersonForm
from .models import Group

# @login_required(login_url='/members/login_user/')
def home(request):
   return render(request, "collect/home.html", {})


def detail(request):
    ...

@login_required
def add_work(request):
    if request.method == "POST":
        form = LoopForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = LoopForm(user=request.user)
    return render(request, "collect/add_work.html", {'form': form})

@login_required
def add_person(request):
    if request.method == "POST":
        form = PersonForm(request.POST)
        instance = form.save(commit=False)
        if not hasattr(instance, "group"):
            group = Group.objects.create(name=instance.first_name, author=request.user)
            instance.group = group
            # print(f"{dir(form.instance)=}")
            # import pdb
            # pdb.set_trace()
        if form.is_valid():
            form.save()
            messages.success(request, "Player added successfully!")
            return redirect('home')

    else:
        form = PersonForm()
    return render(request, "collect/add_person.html", {'form': form})
