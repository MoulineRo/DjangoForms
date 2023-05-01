from django.urls import path

from . import views

urlpatterns = [
    path('groups/', views.groups, name='groups'),
    path('group/', views.group, name='group'),
    path('teachers/', views.teachers, name='teachers'),
    path('teacher/', views.teacher, name='teacher'),
]
