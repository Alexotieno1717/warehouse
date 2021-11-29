from django.db import models
from datetime import datetime


# Create your models here.
class Suppliers(models.Model):
    supplier_name = models.CharField(max_length=200)
    contact_person = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=30)
    supplier_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.supplier_name
