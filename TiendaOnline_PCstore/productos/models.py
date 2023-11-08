from django.db import models

# Create your models here.
class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.TextField(null=False, max_length=50)
    descripcion = models.TextField(null=False, max_length=200)
    precio = models.DecimalField(null=False, max_digits=9, decimal_places=2)  # Agregando max_digits

    def __str__(self):
        return self.nombre
    
    
