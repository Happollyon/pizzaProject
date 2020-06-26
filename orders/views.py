from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login as login_2, logout as logout_2
from django.contrib.auth.models import User
from django.urls import reverse
from .models import user_reg_pizza,user_sici_pizza,user_pasta,user_salad,user_sub,user_plater
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
    user = User.objects.get(id=json_data['user_id'])
    pizza = Regular_pizza.objects.get(id=json_data['item_id'])
    toppin=[0]*5


    for i in range(0,5):


        if len(json_data['tp'])-1 >= i :
          toppin[i] = Topping.objects.get(id=json_data['tp'][i])

        else:

            toppin[i]=Topping.objects.get(id=21)




    user_reg_pizza.objects.create(user_id=user,size=json_data['item_size'],item_id=pizza,option_1=toppin[0],option_2=toppin[1],option_3=toppin[2],option_4=toppin[3],option_5=toppin[4])

    return HttpResponse('e')

def sici_pizza(request):

    #top= request.POST.getlist('data')
    json_data = json.loads(request.body)
    toppin=[0]*5
    user = User.objects.get(id=json_data['user_id'])
    pizza = Sicillia_pizza.objects.get(id=json_data['item_id'])
    print(json_data['tp'])
    for i in range(0, 5):

        if len(json_data['tp']) - 1 >= i:
            toppin[i] = Topping.objects.get(id=json_data['tp'][i])

        else:

            toppin[i] = Topping.objects.get(id=21)



    user_sici_pizza.objects.create(user_id=user,size=json_data['item_size'],item_id=pizza,option_1=toppin[0],option_2=toppin[1],option_3=toppin[2],option_4=toppin[3],option_5=toppin[4])

    return HttpResponse('e')
def pasta(request):
    json_data = json.loads(request.body)
    user = User.objects.get(id=json_data['user_id'])
    pasta = Pasta.objects.get(id=json_data['item_id'])
    user_pasta.objects.create(user_id=user,item_id=pasta)
    return HttpResponse('e')

def salad(request):
    json_data = json.loads(request.body)
    user = User.objects.get(id=json_data['user_id'])
    salad = Salad.objects.get(id=json_data['item_id'])
    user_salad.objects.create(user_id=user, item_id=salad   )
    return HttpResponse('e')

def plater(request):
    json_data = json.loads(request.body)
    user = User.objects.get(id=json_data['user_id'])
    plater = Plater.objects.get(id=json_data['item_id'])
    user_plater.objects.create(user_id=user,item_id=plater,size=json_data['item_size'])
    return HttpResponse('e')

def subs(request):
    json_data = json.loads(request.body)
    user = User.objects.get(id=json_data['user_id'])
    subs = Subs.objects.get(id=json_data['item_id'])
    user_sub.objects.create(user_id=user,item_id=subs,size=json_data['item_size'])
    return HttpResponse('e')


def basket(request,user_id):
    user=user_id
    context={
            "reg_pizza": user_reg_pizza.objects.filter(user_id=user),
            "sici_pizza":user_sici_pizza.objects.filter(user_id=user),
            "subs":user_sub.objects.filter(user_id=user),
            "pasta":user_pasta.objects.filter(user_id=user),
            "salad":user_salad.objects.filter(user_id=user)
        }

    return   render(request,"orders/basket.html",context)