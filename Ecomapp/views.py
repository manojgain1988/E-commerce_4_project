from django.shortcuts import render
from Ecomapp.models import Setting
from Products.models import Product

# Create your views here.

def Index(request):
    setting = Setting.objects.get(id=1)
    products = Product.objects.all().order_by('id')[:4]
    latest_products = Product.objects.all().order_by('-id')
    featured_products = Product.objects.all()
    
    context={
        'setting':setting,
        'products':products,
        'latest_products':latest_products,
        'featured_products':featured_products,
    }
    return render(request,'home.html',context)  


def product_signle(request,id):
    setting = Setting.objects.get(id=1)
    product_signle = Product.objects.get(id=id)
    context = {
        'setting':setting,
        'product_signle':product_signle,
    }
    return render(request,'product-single.html',context)