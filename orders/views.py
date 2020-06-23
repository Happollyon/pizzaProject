from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login as login_2, logout as logout_2
from django.contrib.auth.models import User
from django.urls import reverse
from .models import user_reg_pizza,user_sici_pizza,user_pasta,user_salad
import json

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
            "Subs":Subs.objects.all(),

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

def reg_pizza(request):

    #top= request.POST.getlist('data')
    json_data = json.loads(request.body)
    print(json_data)
    toppin=[0]*5

    for i in range(0,4):
        print(i)
        #print(json_data['tp'][i])
        #print(len(json_data['tp']))
        if len(json_data['tp'])-1 >= i :
          toppin[i] = json_data['tp'][i]
        else:
            print('else')
            toppin[i]=0



    foo_instance = user_reg_pizza.objects.create(user_id=json_data['user_id'],size=json_data['item_size'],item_id=json_data['item_id'],option_1=toppin[0],option_2=toppin[1],option_3=toppin[2],option_4=toppin[3],option_5=toppin[4])

    return HttpResponse('e')

def sici_pizza(request):

    #top= request.POST.getlist('data')
    json_data = json.loads(request.body)
    print(json_data)
    toppin=[0]*5

    for i in range(0,4):
        print(i)
        #print(json_data['tp'][i])
        #print(len(json_data['tp']))
        if len(json_data['tp'])-1 >= i:
          toppin[i] = json_data['tp'][i]
        else:
            print('else')
            toppin[i]=0



    foo_instance = user_sici_pizza.objects.create(user_id=json_data['user_id'],size=json_data['item_size'],item_id=json_data['item_id'],option_1=toppin[0],option_2=toppin[1],option_3=toppin[2],option_4=toppin[3],option_5=toppin[4])

    return HttpResponse('e')
def pasta(request):
    json_data = json.loads(request.body)
    print(json_data)
    user_pasta.objects.create(user_id=json_data['user_id'],item_id=json_data['item_id'])
    return HttpResponse('e')

def salad(request):
    json_data = json.loads(request.body)
    print(json_data)
    user_salad.objects.create(user_id=json_data['user_id'],item_id=json_data['item_id'])
    return HttpResponse('e')