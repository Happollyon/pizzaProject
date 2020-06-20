from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login as login_2, logout as logout_2
from django.contrib.auth.models import User
from django.urls import reverse

# Create your views here.
from .models import Pasta,Topping,Plater,Regular_pizza,Salad,Sicillia_pizza,Subs
def index(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("menu"))
    return render(request, 'orders/index.html')

def login(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login_2(request,user)
        context={"user":user}

        return HttpResponseRedirect(reverse("menu"),context)
    else:
        return render(request, "orders/index.html")

def menu(request):

    if  request.user.is_authenticated:

        context={
            "Regular_pizza":Regular_pizza.objects.all(),
            "Sicillian_pizza":Sicillia_pizza.objects.all(),
            "Topping":Topping.objects.all(),
            "Pasta":Pasta.objects.all(),
            "Salad":Salad.objects.all(),
            "Plater":Plater.objects.all(),
            "Subs":Subs.objects.all()
            }
        return render(request,'orders/menu.html',context)
    else:
        return render(request,"orders/index.html")

def register(request):
    return render(request,"orders/register.html")


def create(request):
    username = request.POST["username"]
    email = request.POST["email"]
    password = request.POST["password"]

    user = User.objects.create_user(username, email,password)
    print('okay')
    return HttpResponseRedirect(reverse("index"))

def logout(request):

    logout_2(request)
    return HttpResponseRedirect(reverse("index"))