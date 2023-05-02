from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import Teachers, Group
from .models import TeachersM, GroupM


def teacher(request):
    if request.method == "POST":
        form = Teachers(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            surname = form.cleaned_data['surname']
            lastname = form.cleaned_data['lastname']
            birthday = form.cleaned_data['birthday']
            theme = form.cleaned_data['theme']
            TeachersM.objects.create(name=name, surname=surname, lastname=lastname, birthday=birthday, theme=theme)
            return HttpResponseRedirect("/teachers/")
    else:
        form = Teachers()
    return render(request, "teacher.html", {"form": form})


def teachers(request):
    if request.method == "GET":
        people = TeachersM.objects.all()
        return render(request, "teachers.html", {"people": people})


#

def group(request):
    if request.method == "POST":
        form = Group(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            GroupM.objects.create(name=name)
            return HttpResponseRedirect("/groups/")
    else:
        form = Group()
    return render(request, "group.html", {"form": form})


def groups(request):
    if request.method == "GET":
        groupe = GroupM.objects.all()
        return render(request, "teachers.html", {"people": groupe})
