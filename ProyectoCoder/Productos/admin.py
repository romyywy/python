from django.contrib import admin
from Productos import models

# Register your models here.
admin.site.register(models.Product)
admin.site.register(models.Cliente)
admin.site.register(models.Vendedor)