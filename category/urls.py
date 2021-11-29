from django.urls import path

from . import views

urlpatterns = [
    path('', views.category_add, name='category_add'),
    path('category_list/', views.category_list, name='category_list'),
]
