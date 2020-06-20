from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("menu",views.menu, name="menu"),
    path("login",views.login, name="login"),
    path("create",views.create,name='create'),
    path("register", views.register, name="register"),
    path("logout", views.logout, name="logout"),
]
urlpatterns+= staticfiles_urlpatterns()
