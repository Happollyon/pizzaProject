from django.contrib import admin
from .models import Plater,Pasta,Salad,Topping,Regular_pizza,Sicillia_pizza,Subs

# Register your models here.
admin.site.register(Pasta)
admin.site.register(Plater)
admin.site.register(Salad)
admin.site.register(Topping)
admin.site.register(Regular_pizza)
admin.site.register(Sicillia_pizza)
admin.site.register(Subs)

