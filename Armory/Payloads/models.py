from django.db import models

# Create your models here.

class ReturnedCipher(models.Model):
    returned = models.CharField(max_length=245, default='')

class Seed1(models.Model):
    seed_1 = models.IntegerField(default=1)
    seed_2 = models.IntegerField(default=1)
    inherited = models.ForeignKey (
        ReturnedCipher, on_delete=models.CASCADE
    )
    
class Response(models.Model):
    cipher = models.CharField(max_length=233, default=None)
    depth = models.IntegerField(default=0)
    
class TypeSync(models.Model):
    login = models.BooleanField(default=True)
    
class type(models.Model):
    qr = models.BooleanField(default=False)
    
    
