from distutils.command.sdist import sdist
from django.db import models
from django.forms import CharField

# Create your models here.

class Hashes(models.Model):
    sha1 = models.CharField(max_length=245, default='')
    md5 = models.CharField(max_length=245, default='')
    gtr_245 = models.BooleanField(default=False)

# class Wordlists(models.Model):
#     passwords = models.FileField(storage=)
#     pins = models.Filefield(storage=)