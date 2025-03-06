from django.shortcuts import render, get_object_or_404

from .models import Person

# Create your views here.

#List of all the people that exist in the database
def dashboard(request):
    people = Person.objects.all()
    return render(request , "../templates/dashboard.html" , {"people" : people})

#Products for each person
def person_products(request, person_id):
    person = get_object_or_404(Person, id = person_id)
    products = person.products
    return render(request, "../templates/person_products.html", {"person": person , "products": products})