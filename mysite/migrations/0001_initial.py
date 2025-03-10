# Generated by Django 5.1.6 on 2025-03-06 02:41

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('age', models.IntegerField(validators=[django.core.validators.MinValueValidator(18), django.core.validators.MaxValueValidator(100)])),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('position', models.CharField(choices=[('Manager', 'MA'), ('Engineer', 'EG'), ('Accountant', 'ACC'), ('HR', 'HR'), ('Media', 'M'), ('Marketing', 'MKT')], max_length=10)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('edited_at', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('product_type', models.CharField(choices=[('Electronics', 'Electronics'), ('Furniture', 'Furniture'), ('Clothing', 'Clothing'), ('Other', 'Other')], max_length=20)),
                ('serial_code', models.CharField(max_length=20, unique=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.person')),
            ],
        ),
    ]
