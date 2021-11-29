from django.shortcuts import render


# Create your views here.
def product_add(request):
    return render(request, 'products/product.html')


def product_list(request):
    return render(request, 'products/product_list.html')
