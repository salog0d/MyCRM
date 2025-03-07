from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib import messages

from .models import Person, Product
from .forms import PersonForm, ProductForm

#Read opperations
#List of all the people that exist in the database
def dashboard(request):
    people = Person.objects.all()
    return render(request , "../templates/dashboard.html" , {"people" : people})

#Products for each person
def person_products(request, person_id):
    person = get_object_or_404(Person, id = person_id)
    products = person.products
    return render(request, "../templates/person/person_products.html", {"person": person , "products": products})

#Person full details
#Renders the view in which al details from this product can be seen
def person_details(request, person_id):
    person = get_object_or_404(Person , id = person_id)
    personal_info = [person.name, person.last_name, person.age, person.email, person.position]
    return render(request, "../templates/person/person_details.html", {"person": person , "personal_info": personal_info})


def product_details(request, person_id, product_id):
    person = get_object_or_404(Person, id=person_id)
    product = get_object_or_404(Product, id=product_id, owner=person)  # Ensure the product belongs to the person

    return render(request, "product/product_detail.html", {
        "person": person,
        "product": product,  
    })
#Create opperations

def create_person(request):
    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Person created succesfully.")
            return redirect("dashboard")
    else:
        form = PersonForm()

    return render(request, "../templates/person/person_form.html", {"form": form, "action": "Create"})

def create_product(request, person_id):
    person = get_object_or_404(Person, id= person_id)
    if request.method == "POST":
        # Crear una instancia del formulario con los datos enviados
        form = ProductForm(request.POST)
        if form.is_valid():
            # Guardar el producto en la base de datos
            product = form.save(commit=False)
            product.owner =  person
            product.save()
            messages.success(request, "Producto creado exitosamente.")
            return redirect("dashboard")  # Redirigir al dashboard o a la lista de productos
        else:
            # Si el formulario no es válido, mostrar errores
            messages.error(request, "Por favor, corrige los errores en el formulario.")
    else:
        # Si no es una solicitud POST, mostrar el formulario vacío
        form = ProductForm()
    
    # Renderizar el formulario en la plantilla
    return render(request, "../templates/product/product_form.html", {"form": form, "action": "Crear"})

#Update opperations

def update_person(request, person_id):
    # Obtener la persona que se va a actualizar
    person = get_object_or_404(Person, id=person_id)
    
    if request.method == "POST":
        # Crear una instancia del formulario con los datos enviados y la instancia de la persona
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            # Guardar los cambios en la base de datos
            form.save()
            messages.success(request, "Persona actualizada exitosamente.")
            return redirect("dashboard")  # Redirigir al dashboard o a la lista de personas
        else: 
            # Si el formulario no es válido, mostrar errores
            messages.error(request, "Por favor, corrige los errores en el formulario.")
    else:
        # Si no es una solicitud POST, mostrar el formulario prellenado con los datos actuales
        form = PersonForm(instance=person)
    
    # Renderizar el formulario en la plantilla
    return render(request, "person/person_form.html", {
        "form": form,
        "action": "Actualizar",
        "person": person,  # Pasar la persona al contexto para usarla en la plantilla
    })
def update_product(request, person_id, product_id):
    return

#Delete opperations

def delete_person(request, person_id):
    return

def delete_product(request, person_id):
    return
