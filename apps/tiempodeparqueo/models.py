from django.db import models

# Create your models here.
class Tiempodeparqueo (models.Model):
    entryTime= models.TextField("entryTime", blank=True, null=True)
    exitTime= models.TextField("exitTime", blank=True, null=True)
    rate= models.TextField("rate", blank=True, null=True)
    placa= models.TextField("placa", blank=True, null=True)

    def __str__(self):
        return f'{self.entryTime}'
    
    def __str__(self):
        return f'{self.exitTime}'
    
    def __str__(self):
        return f'{self.rate}'
    
    def __str__(self):
        return f'{self.placa}'
    