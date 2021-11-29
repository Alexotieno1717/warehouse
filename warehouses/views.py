from django.shortcuts import render


# Create your views here.
def warehouse_add(request):
    return render(request, 'warehouse/warehouse.html')


def warehouse_list(request):
    return render(request, 'warehouse/warehouse_list.html')
