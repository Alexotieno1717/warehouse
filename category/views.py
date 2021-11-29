from django.shortcuts import render


# Create your views here.
def category_add(request):
    return render(request, 'category/category.html')


def category_list(request):
    return render(request, 'category/category_list.html')
