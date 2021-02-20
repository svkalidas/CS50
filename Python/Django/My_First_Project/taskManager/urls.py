from django.urls import path
from . import views


app_name = "task"
urlpatterns=[
    path("",views.index, name="index"),
    path("welcome",views.welcome, name="welcome"),
    path("add",views.add, name="add"),
    path("clear", views.clear, name="clear")
]