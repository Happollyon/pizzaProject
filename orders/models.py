from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Pasta(models.Model):

    name= models.CharField(max_length=64,default='teste')
    price= models.FloatField(default=0)

    def __str__(self):
        return f"{self.name}  {self.price} euros"


class Salad(models.Model):
    name=models.CharField(max_length=64,default='teste')
    price=models.FloatField(default=0)
    def __str__(self):
        return f"{self.name}  {self.price} euros"

class Plater(models.Model):
    name=models.CharField(max_length=64,default='teste')
    price1=models.FloatField(default=0)
    price2=models.FloatField(default=0)
    def __str__(self):
        return f"{self.name}  {self.price1} small  {self.price2} large"

class Topping(models.Model):
    name= models.CharField(max_length=64, default='teste')

    def __str__(self):
        return f"{self.name}"

class Regular_pizza(models.Model):
    name= models.CharField(max_length=64, default='teste')
    price1=models.FloatField(default=0)
    price2=models.FloatField(default=0)
    option=models.IntegerField(default=0)

    def __str__(self):
        return  f"{self.name} {self.price1} small {self.price2} large"

class Sicillia_pizza(models.Model):
    name = models.CharField(max_length=64, default='teste')
    price1 = models.FloatField(default=0)
    price2 = models.FloatField(default=0)
    option = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name} {self.price1} small {self.price2} large"
class Subs(models.Model):
    name = models.CharField(max_length=64, default='teste')
    price1 = models.FloatField(default=0)
    price2 = models.FloatField(default=0)
    option = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name} {self.price1} small {self.price2} large"

class user_reg_pizza(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    item_id = models.ForeignKey(Regular_pizza,on_delete=models.CASCADE)
    size = models.CharField(max_length=64,default='teste')
    option_1 = models.ForeignKey(Topping,on_delete=models.CASCADE , related_name='toppiqqerng1')
    option_2 = models.ForeignKey(Topping, on_delete=models.CASCADE, related_name='topping2')
    option_3 = models.ForeignKey(Topping, on_delete=models.CASCADE, related_name='toppifaerwng3')
    option_4 = models.ForeignKey(Topping, on_delete=models.CASCADE, related_name='toppdafweing4')
    option_5 = models.ForeignKey(Topping, on_delete=models.CASCADE, related_name='topdfasfping5')


class user_sici_pizza(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE, related_name='user')
    item_id = models.ForeignKey(Regular_pizza,on_delete=models.CASCADE, related_name='pizza_id')
    size = models.CharField(max_length=64,default='teste')
    first_option = models.ForeignKey(Topping,on_delete=models.CASCADE, related_name='adfa')
    second_option = models.ForeignKey(Topping, on_delete=models.CASCADE, related_name='fasfae')
    third_option = models.ForeignKey(Topping, on_delete=models.CASCADE, related_name='slfkgs')
    forth_option = models.ForeignKey(Topping, on_delete=models.CASCADE, related_name='toppierqsng4')
    fifth_option = models.ForeignKey(Topping, on_delete=models.CASCADE, related_name='toppifadsfaang5' )

