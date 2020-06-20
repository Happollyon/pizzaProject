from django.db import models

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