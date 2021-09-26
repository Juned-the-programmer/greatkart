from django.shortcuts import render , get_object_or_404
from .models import *
from category.models import Category

# Create your views here.
def store(request , category_slug=None):

    categories = None
    products = None

    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug) 
        produt_data = Product.objects.filter(category=categories , is_available=True)
        produt_data_count = produt_data.count()
    else:
        produt_data = Product.objects.all().filter(is_available=True)
        produt_data_count = produt_data.count()

    category_data = Category.objects.all()
    context = {
        'product_data' : produt_data,
        'product_data_count' : produt_data_count,
        'category_data' : category_data
    }
    return render(request, 'store/store.html',context)

def product_details(request , category_slug , product_slug):
    try:
        single_product = Product.objects.get(category__slug=category_slug , slug=product_slug)
    except Exception as e:
        raise e

    context = {
        'single_product': single_product,
    }
    return render(request, 'store/detail.html',context)