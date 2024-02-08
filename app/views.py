from django.shortcuts import render, get_object_or_404
from .models import SubProducts,ProductDetails

# Create your views here.
def my_view(request):
        sub_products = SubProducts.objects.all()
        return {'SubProducts': sub_products}

def home(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def product(request, pk):
    sub_product = get_object_or_404(SubProducts, pk=pk)
    products = ProductDetails.objects.filter(category=sub_product)
    return render(request, "product.html", {'sub_product': sub_product, 'products': products})




