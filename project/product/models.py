from django.db import models


class Products(models.Model):
    name = models.CharField(max_length=30)
    detail = models.TextField()
    price = models.FloatField(default=0.00)
    quantity = models.PositiveSmallIntegerField(default=0)
    seller = models.CharField(max_length=30)
