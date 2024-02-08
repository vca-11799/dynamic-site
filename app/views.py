from django.shortcuts import render
from .models import SubProducts

# Create your views here.
def home(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def product(request):
    return render(request, "product.html")

def my_view(request):
        sub_products = SubProducts.objects.all()
        return {'SubProducts': sub_products}



    



