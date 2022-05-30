from hashlib import sha1
from django.db import models

# Create your models here.

class CipherText(models.Model):
    md5 = models.CharField(max_length=245, default='')
    sha1 = models.CharField(max_length=245, default='')

class Seeds(models.Model):
    seed_1 = models.IntegerField(default=1)
    seed_2 = models.IntegerField(default=1)
    inherited = models.ForeignKey (
        CipherText, on_delete=models.CASCADE
    )
    
class Response(models.Model):
    cipher = models.CharField(max_length=233, default=None)
    depth = models.IntegerField(default=0)
    
class TypeSync(models.Model):
    login = models.BooleanField(default=True)
    
class QR(models.Model):
    qrcode = models.BooleanField(default=False)
    

