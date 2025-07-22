from django.shortcuts import render
from .models import Category, Product

from django.shortcuts import render

def test_view(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    return render(request, 'template.html', {
        'categories': categories,
        'products': products,
    })


def home(request):
    return render(request, 'home.html')
