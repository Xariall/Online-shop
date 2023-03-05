from django.shortcuts import render
from .models import *

# Create your views here.
def store(request):
	products = Product.objects.all()
	context = {'products' : products}
	return render(request, 'main/store.html', context)

def cart(request):
	context = {}
	return render(request, 'main/cart.html', context)

def checkout(request):
	context = {}
	return render(request, 'main/checkout.html', context)