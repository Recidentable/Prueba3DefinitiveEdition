from django.db import models

# Create your models here.
class Categoria(models.Model):
    
    idCategoria = models.IntegerField(primary_key=True, verbose_name='Id de categoria')
    nombreCategoria = models.CharField(max_length=50, verbose_name='Nombre de la Categoria')
    
    def __str__(self):
        return self.nombreCategoria
    
#Modelos

class Producto(models.Model):
    
    Id = models.CharField(max_length=6, primary_key=True, verbose_name='Id')
    nombre = models.CharField(max_length=20, verbose_name='nombre')
    precio = models.CharField(max_length=20, verbose_name='precio')
    stock = models.CharField(max_length=4, verbose_name='stock')
    descripcion = models.CharField(max_length=80, verbose_name='descripcion')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.Id