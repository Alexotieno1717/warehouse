from django.urls import path

from . import views

urlpatterns = [
    path('', views.supplier_add, name='supplier_add'),
    path('<int:supply_id>', views.supply, name='supply'),
    path('<int:id>/delete', views.delete_view, name="delete"),
    path('suppliers_list/', views.supplier_list, name='supplier_list'),
]
