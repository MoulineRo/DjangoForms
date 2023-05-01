from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import Teachers, Group
from .models import TeachersM, GroupM


def teacher(request):
    if request.method == "POST":
        form = Teachers(request.POST)
        if form.is_valid():
            q1 = form.cleaned_data['name']
            q2 = form.cleaned_data['surname']
            q3 = form.cleaned_data['lastname']
            q4 = form.cleaned_data['birthday1']
            q5 = form.cleaned_data['birthday2']
            q6 = form.cleaned_data['birthday3']
            q7 = form.cleaned_data['theme']
            TeachersM.objects.create(name=q1, surname=q2, lastname=q3, birthday1=q4, birthday2=q5, birthday3=q6,
                                     theme=q7)
            return HttpResponseRedirect("/teachers/")
    # else як у якості get-запроса
    else:
        form = Teachers()
    return render(request, "teacher.html", {"form": form})


def teachers(request):
    if request.method == "GET":
        people = TeachersM.objects.all()
        list = []
        for person in people:
            list.append(
                f"{person.id} {person.name} {person.surname} {person.lastname} {person.birthday1}/{person.birthday2}/{person.birthday3} - {person.theme}")
        return render(request, "teachers.html", {"people": list})


def group(request):
    if request.method == "POST":
        form = Group(request.POST)
        if form.is_valid():
            q = form.cleaned_data['name']
            GroupM.objects.create(name=q)
            return HttpResponseRedirect("/groups/")
    # else як у якості get-запроса
    else:
        form = Group()
    return render(request, "group.html", {"form": form})


def groups(request):
    if request.method == "GET":
        people = GroupM.objects.all()
        list = []
        for person in people:
            list.append(f"{person.id} {person.name}")
        return render(request, "teachers.html", {"people": list})
