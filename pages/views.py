from django.shortcuts import render
from store.models import *
from category.models import *

# Create your views here.
def index(request):
    product_data = Product.objects.all().filter(is_available=True)
    category_data = Category.objects.all()
    context = {
        'product_data': product_data,
        'category_data': category_data,
    }
    return render(request , "pages/index.html",context)