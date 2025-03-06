from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Person(models.Model):
    POSITION_OPTIONS = [
        ("Manager", "MA"),
        ("Engineer", "EG"),
        ("Accountant", "ACC"),
        ("HR", "HR"),
        ("Media", "M"),
        ("Marketing", "MKT"),
    ]
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField(validators=[MinValueValidator(18), MaxValueValidator(100)])
    email = models.EmailField(unique=True)
    position = models.CharField(choices=POSITION_OPTIONS)
    created_at = models.DateField(auto_now_add=True)
    edited_at = models.DateField(auto_not=True)

    def __str__(self):
        return f"{self.name}-{self.last_name}-{self.age}-{self.email}-{self.position}"

class  Product(models.Model):
    PRODUCT_TYPE = [
        ("Electronics", "Electronics"),
        ("Furniture", "Furniture"),
        ("Clothing", "Clothing"),
        ("Other", "Other"),
    ]
    id = models.AutoField(primary_key=True)
    product_type = models.CharField(choices=PRODUCT_TYPE)
    serial_code = models.CharField(max_length=20, unique=True)
    owner = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product_type}-{self.serial_code}"

