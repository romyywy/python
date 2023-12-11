from django.db import models

# Create your models here.

class Product(models.Model):
    nombre=models.CharField(max_length=50)
    descripcion=models.CharField(max_length=50)
    cantidad_stock=models.IntegerField()

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    correo= models.EmailField()

class Vendedor(models.Model):
    nombre=models.CharField(max_length=50)
    tienda= models.CharField(max_length=50)