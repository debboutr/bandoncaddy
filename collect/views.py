from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .forms import LoopForm, PersonForm
from .models import Course, Party, Loop, Person

from datetime import timedelta
from django.utils import timezone


def home(request):
    today = timezone.now().date()
    week_ago = today - timedelta(days=today.weekday() + 7)
    loops = Loop.objects.order_by("-date")[:4]
    return render(request, "collect/home.html", {"loops": loops})


def detail(request): ...


@login_required
def add_loop(request):
    courses = Course.objects.all()
    if request.method == "POST":
        form = LoopForm(data=request.POST, user=request.user)
        form.instance.author = request.user
        if form.is_valid():
            form.save()
            messages.success(request, "Loop data added successfully!")
            return redirect("home")

    else:
        form = LoopForm(user=request.user)
    return render(request, "collect/add_loop.html", {"form": form, "courses": courses})


@login_required
def edit_loop(request, pk):
    courses = Course.objects.all()
    loop = get_object_or_404(Loop, pk=pk)
    print(f"{loop=}")
    if request.method == "POST":
        form = LoopForm(data=request.POST, user=request.user)
        form.instance.author = request.user
        if form.is_valid():
            form.save()
            messages.success(request, "Loop data updated!")
            return redirect("home")

    else:
        form = LoopForm(instance=loop, user=request.user)
        print(f"{form=}")
    return render(request, "collect/edit_loop.html", {"form": form, "courses": courses})


@login_required
def add_person(request):
    if request.method == "POST":
        form = PersonForm(request.POST)
        instance = form.save(commit=False)
        if not hasattr(instance, "group"):
            full = f"{instance.first_name}-{instance.last_name}".upper()
            group = Party.objects.create(name=full, author=request.user)
            instance.group = group
        if form.is_valid():
            form.save()
            messages.success(request, "Player added successfully!")
            return redirect("home")

    else:
        form = PersonForm()
    return render(request, "collect/add_person.html", {"form": form})


@login_required
def edit_person(request, pk):
    person = get_object_or_404(Person, pk=pk)
    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Player updated!")
            return redirect("home")

    else:
        form = PersonForm(instance=person)
    return render(request, "collect/add_person.html", {"form": form})
