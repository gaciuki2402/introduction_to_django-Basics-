<<<<<<< HEAD
from os import name
from django.urls import path
from polls import views

urlpatterns=[
    path("", views.home, name="polls-home"),
    path("about/", views.about, name="polls-about")
=======
from django.urls import path
<<<<<<< HEAD
from polls import views
urlpatterns = [
    path("",views.index, name="index"),
    path("about/",views.about, name="about"),
=======

from . import views

urlpatterns=[
    path("lib/", views.lib, name="lib"),
>>>>>>> c979997c2e55e1eea0d57b172d424e32f685934d

>>>>>>> eadf4933b17b4f1e48aa6f604a342fb4573953d9
]