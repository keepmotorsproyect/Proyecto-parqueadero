from django.db import models

# Create your models here.
class Tipo_de_factura (models.Model):
    nombre= models.TextField("nombre", blank=True, null=True)
    cedula= models.TextField("cedula", blank=True, null=True)
    correo= models.TextField("correo", blank=True, null=True)
    direccion= models.TextField("direccion", blank=True, null=True)
    banco= models.TextField("banco", blank=True, null=True)


    def __str__(self):
        return f'{self.nombre}'
    
    def __str__(self):
        return f'{self.cedula}'
    
    def __str__(self):
        return f'{self.correo}'
    
    def __str__(self):
        return f'{self.direccion}'
    
    def __str__(self):
        return f'{self.banco}'
