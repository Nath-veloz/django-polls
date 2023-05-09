from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('sobre/', views.sobre, name='sobre')
]

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
]