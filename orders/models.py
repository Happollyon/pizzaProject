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
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reg_pizza_client')
    item_id = models.ForeignKey(Regular_pizza, on_delete=models.CASCADE, related_name='item')
    size = models.CharField(max_length=64, default='teste')
    option_1 = models.ForeignKey(Topping, on_delete=models.CASCADE, related_name='topping1')
    option_2 = models.ForeignKey(Topping, on_delete=models.CASCADE, related_name='topping2')
    option_3 = models.ForeignKey(Topping, on_delete=models.CASCADE, related_name='topping3')
    option_4 = models.ForeignKey(Topping, on_delete=models.CASCADE, related_name='topping4')
    option_5 = models.ForeignKey(Topping, on_delete=models.CASCADE, related_name='topping5')



class user_sici_pizza(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sici_pizza_client')
    item_id = models.ForeignKey(Sicillia_pizza, on_delete=models.CASCADE, related_name='item')
    size = models.CharField(max_length=64, default='teste')
    option_1 = models.ForeignKey(Topping, on_delete=models.CASCADE, related_name='topping_added_1')
    option_2 = models.ForeignKey(Topping, on_delete=models.CASCADE, related_name='topping_added_2')
    option_3 = models.ForeignKey(Topping, on_delete=models.CASCADE, related_name='topping_added_3')
    option_4 = models.ForeignKey(Topping, on_delete=models.CASCADE, related_name='topping_added_4')
    option_5 = models.ForeignKey(Topping, on_delete=models.CASCADE, related_name='topping_added_5')
class user_pasta(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE,related_name='pasta_client')
    item_id = models.ForeignKey('Pasta',on_delete=models.CASCADE,related_name='item')

class user_salad(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='salad_client')
    item_id = models.ForeignKey('Salad', on_delete=models.CASCADE, related_name='item')


class user_plater(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='plater_client')
    item_id = models.ForeignKey('Plater', on_delete=models.CASCADE, related_name='item')
    size = models.CharField(default='teste',max_length=64)

class user_sub(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sub_client')
    item_id = models.ForeignKey('Subs', on_delete=models.CASCADE, related_name='item')
    size = models.CharField(default='teste',max_length=64)



