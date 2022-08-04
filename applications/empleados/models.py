from django.db import models

class employee(models.Model):
    name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    email=models.EmailField(max_length = 254)
    phone=models.CharField(max_length=30)
    
    def __str__(self):
        return self.name+'-'+self.last_name+'-'+self.email+'-'+self.phone