from django.urls import path
from Ecomapp import views


urlpatterns = [
    path('', views.Index, name='index'),
    path('product_signle/<int:id>', views.product_signle, name='product_signle'),
]