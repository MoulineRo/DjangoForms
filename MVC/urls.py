from django.contrib import admin
from django.urls import path
from polls import views

urlpatterns = [
    path('groups/', views.groups),
    path('group/', views.group),
    path('teachers/', views.teachers),
    path('teacher/', views.teacher),
    path('admin/', admin.site.urls),
]
