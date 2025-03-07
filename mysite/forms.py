from django import forms
from .models import Person, Product
from django.utils import timezone

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'last_name', 'age', 'email', 'position']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'position': forms.Select(attrs={'class': 'form-control'}),
        }

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.edited_at = timezone.now().date()
        if commit:
            instance.save()
        return instance

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_type', 'serial_code', 'name', 'quantity']
        widgets = {
            'product_type': forms.Select(attrs={'class': 'form-control'}),
            'serial_code': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
        }