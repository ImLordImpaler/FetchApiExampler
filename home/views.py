from django.shortcuts import render
from .models import Products
from django.http import JsonResponse
# Create your views here.
def index(request):
    products = Products.objects.all()
    params = {
        'products': products,
    }
    return render(request , 'home/index.html' , params)


def productDetail(request , pk):
    products = Products.objects.get(id = pk)
    
    params = {
        'products' : products

    }
    return render(request , 'home/product.html' , params)

def updateItem(request):
    return JsonResponse('Item was added!' , safe=False)