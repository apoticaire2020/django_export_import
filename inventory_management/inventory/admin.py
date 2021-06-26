from django.contrib import admin
from .models import Product,Laptop,Desktop,Mobile

# Register your models here.

@admin.register(Product , Laptop , Desktop , Mobile)
class ViewAdmin(admin.ModelAdmin):
    pass

