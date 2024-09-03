from django.db import models

# Create your models here.
# Se crean las tablas automaticamente (ORM)

class Clientes(models.Model):
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50, verbose_name="La Dirección")  #Le cambia el nombre al campo de como se muestra en el Panel A
    email = models.EmailField(blank=True, null=True)    #Campo para emails #Se colocan estos campos para que no se obligatorio añadir en el panel de admin
    telefono = models.CharField(max_length=7)

    def __str__(self):
        return self.nombre

class Articulos(models.Model):
    nombre = models.CharField(max_length=30)
    seccion = models.CharField(max_length=20)
    precio = models.IntegerField()

    def __str__(self):
        return 'El nombre es %s la seccion es %s y el precio es %s' %(self.nombre, self.seccion, self.precio)


class Pedidos(models.Model):
    numero = models.IntegerField()
    fecha = models.DateField()
    entregado = models.BooleanField()




