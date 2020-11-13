from django.db import models

# Create your models here.
class Vivero(models.Model):
    nombre = models.CharField(max_length=80,verbose_name="Nombre")
    propietario = models.CharField(max_length=80,verbose_name="Propietario")
    direccion = models.CharField(max_length=150, verbose_name="Direccion")
    numero_telefono = models.CharField(max_length=100,verbose_name="Numero_telefono")
    correo = models.CharField(max_length=50,verbose_name="Correo")
    
    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name='vivero'
        verbose_name_plural ='viveros'


class Plantas(models.Model):
    nombre = models.CharField(max_length=80,verbose_name="Nombre")
    precio = models.CharField(max_length=50, verbose_name="Precio")
    tipo_variedad = models.CharField(max_length=100,verbose_name="Tipo_variedad")
    altura = models.CharField(max_length=50,verbose_name="Altura")
    
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name='Planta'
        verbose_name_plural ='plantas'
        

class Cliente(models.Model):
    nombre = models.CharField(max_length=80, verbose_name='Nombre')
    apellidos = models.CharField(max_length=80, verbose_name='Apellidos(s)')
    telefono= models.CharField(max_length=20, verbose_name='Telefono')
    correo = models.CharField(max_length=100, verbose_name='Correo electronico')
    direccion = models.CharField(max_length=100, verbose_name='Direccion')

    def __str__(self):
        return self.nombre
class Meta:
            verbose_name= 'Cliente'
            verbose_name_plural= 'Clientes'
class Vendedor(models.Model):
    nombre = models.CharField(max_length=80, verbose_name='Nombre')
    apellidos = models.CharField(max_length=80, verbose_name='Apellidos(s)')
    telefono= models.CharField(max_length=20, verbose_name='Telefono')
    correo = models.CharField(max_length=100, verbose_name='Correo electronico')
    direccion = models.CharField(max_length=100, verbose_name='Direccion')

    def __str__(self):
        return self.nombre
class Meta:
            verbose_name= 'Vendedor'
            verbose_name_plural= 'Vendedores'

class Proveedor(models.Model):
    nombre = models.CharField(max_length=80, verbose_name='Nombre')
    apellidos = models.CharField(max_length=80, verbose_name='Apellidos(s)')
    telefono = models.CharField(max_length=20, verbose_name='Telefono')
    correo = models.CharField(max_length=100, verbose_name='Correo electronico')
    direccion = models.CharField(max_length=100, verbose_name='Direccion')

    def __str__(self):
        return "{0} {1} :: {2}".format(self.nombre, self.apellidos, self.direccion)
    class Meta:
        verbose_name= 'Proveedor'
        verbose_name_plural= 'Proveedores'








    