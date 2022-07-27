from django.db import models

# Create your models here.
class products(models.Model):
    # idi=models.CharField(max_length=120,default='')
    typei = models.CharField(max_length=120, default='')
    category = models.CharField(max_length=120, default='')
    tittle=models.CharField(max_length=120,default='')
    qty=models.IntegerField()
    price=models.FloatField()
    description=models.TextField(blank=True,null=True)

