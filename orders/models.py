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
    user_id = models.IntegerField(default=0)
    item_id = models.IntegerField(default=0)
    size = models.CharField(max_length=64,default='teste')
    option_1 =models.IntegerField(default=0)
    option_2 = models.IntegerField(default=0)
    option_3 = models.IntegerField(default=0)
    option_4 = models.IntegerField(default=0)
    option_5 = models.IntegerField(default=0)


class user_sici_pizza(models.Model):
    user_id = models.IntegerField(default=0)
    item_id = models.IntegerField(default=0)
    size = models.CharField(max_length=64, default='teste')
    option_1 = models.IntegerField(default=0)
    option_2 = models.IntegerField(default=0)
    option_3 = models.IntegerField(default=0)
    option_4 = models.IntegerField(default=0)
    option_5 = models.IntegerField(default=0)
class user_pasta(models.Model):
    user_id = models.IntegerField(default=0)
    item_id = models.IntegerField(default=0)

class user_salad(models.Model):
    user_id = models.IntegerField(default=0)
    item_id = models.IntegerField(default=0)


class user_plater(models.Model):
    user_id = models.IntegerField(default=0)
    item_id = models.IntegerField(default=0)
    size = models.CharField(default='teste',max_length=64)

class user_sub(models.Model):
    user_id = models.IntegerField(default=0)
    item_id = models.IntegerField(default=0)
    size = models.CharField(default='teste',max_length=64)



