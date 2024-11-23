from django.shortcuts import render
from Ecomapp.models import Setting
from Products.models import Product

# Create your views here.

def Index(request):
    setting = Setting.objects.get(id=1)
    products = Product.objects.all().order_by('id')[:4]
    context={
        'setting':setting,
        'products':products,
    }
    return render(request,'home.html',context)  