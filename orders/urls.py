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
    path("reg_pizza", views.reg_pizza, name="reg_pizza"),
    path("<int:topping>", views.reg_pizza)
]
urlpatterns+= staticfiles_urlpatterns()
