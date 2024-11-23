from django.urls import path
from Ecomapp import views


urlpatterns = [
    path('', views.Index, name='index')
]