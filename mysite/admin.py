# mysite/admin.py
from django.contrib import admin
from .models import Person, Product

admin.site.register(Person)
admin.site.register(Product)