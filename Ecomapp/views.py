from django.shortcuts import render
from Ecomapp.models import Setting
from Products.models import Product,Images

# Create your views here.

def Index(request):
    setting = Setting.objects.get(id=1)
    sliding_images = Product.objects.all().order_by('id')[:4]
    latest_products = Product.objects.all().order_by('-id')
    featured_products = Product.objects.all()
    
    context={
        'setting': setting,
        'sliding_images': sliding_images,
        'latest_products': latest_products,
        'featured_products': featured_products,
    }
    return render(request,'home.html',context)  


def product_signle(request,id):
    setting = Setting.objects.get(id=1)
    single_product = Product.objects.get(id=id)
    images = Images.objects.filter(product_id=id)
    products = Product.objects.all().order_by('id')[:4]
    context = {
        'setting': setting,
        'single_product': single_product,
        'images': images,
        'products': products,
    }
    return render(request,'product-single.html',context)