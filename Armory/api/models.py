from django.db import models

# Create your models here.

class Table(models.Model):
    case1 = models.CharField(max_length=245, default='')
    case2 = models.CharField(max_length=245, default='')
    case3 = models.CharField(max_length=245, default='')
    case4 = models.CharField(max_length=245, default='')
    case5 = models.CharField(max_length=245, default='')
    case6 = models.CharField(max_length=245, default='')
