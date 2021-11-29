from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect
import sweetify
from .models import Suppliers


# Create your views here.
def supplier_add(request):
    if request.method == 'POST':
        post = Suppliers()
        post.supplier_name = request.POST.get('supplier_name')
        post.contact_person = request.POST.get('contact_person')
        post.email = request.POST.get('email')
        post.phone = request.POST.get('phone')
        post.address = request.POST.get('address')
        post.save()
        args2 = dict(title='Warehouse', icon='success', text="You have Added Supplier", button="Ok")
        sweetify.multiple(request, args2)
        return render(request, 'supplier/supplier.html')
    else:
        return render(request, 'supplier/supplier.html')


def supply(request, supply_id):
    supplied = get_object_or_404(Suppliers, pk=supply_id)
    if request.method == 'POST':
        supplied.supplier_name = request.POST['supplier_name']
        supplied.contact_person = request.POST['contact_person']
        supplied.email = request.POST['email']
        supplied.phone = request.POST['phone']
        supplied.address = request.POST['address']

        supplied.save()
        args2 = dict(title='Warehouse', icon='success', text="You have Updated the Supplier successfully", button="Ok")
        sweetify.multiple(request, args2)
        return redirect('suppliers_list/')

    context = {
        'supplied': supplied
    }

    return render(request, 'supplier/supply.html', context)


def supplier_list(request):
    suppliers = Suppliers.objects.order_by('-supplier_date')
    context = {
        'suppliers': suppliers
    }
    return render(request, 'supplier/supplier_tables.html', context)


def delete_view(request, id):
    if request.method == "POST":
        delete_supply = Suppliers.objects.get(id=id)
        delete_supply.delete()
        args2 = dict(title='Warehouse', icon='success', text="Supplier deleted successfully", button="ok")
        sweetify.multiple(request, args2)
        return HttpResponseRedirect('/')

