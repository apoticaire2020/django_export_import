from django.shortcuts import render
from .models import *

from .resources import ProductResource
from django.contrib import messages
from tablib import Dataset
from django.http import HttpResponse

def simple_upload(request):
    if request.method  == 'POST':
        productResource = ProductResource()
        dataset = Dataset
        new_product = request.FILES['myfile']
        
        if not new_product.name.endswith('xlsx'):
            messages.info(request ,'wrong format')
            return render(request , 'uplated.html')
        imported_data = dataset.load(new_product.read(),format='xlsx')
        for data in imported_data:
            value = Product(
                data[0],
                data[1],
                data[2],
                data[3],
                data[4],
                data[5],
                data[6]
                )
            value.save()
    return render(request , 'uplated.html')
        
            
        


# Create your views here.

def index(request):
    return render(request , 'index.html')

def display_laptops(request):
    items = Laptop.objects.all()
    context = {
        'items':items ,
    }
    return render(request , 'index.html' , context)

def display_desktops(request):
    items = Desktop.objects.all()
    context = {
        'items':items ,
    }
    return render(request , 'index.html' , context)

def display_mobiles(request):
    items = Mobile.objects.all()
    context = {
        'items':items ,
    }
    return render(request , 'index.html' , context)