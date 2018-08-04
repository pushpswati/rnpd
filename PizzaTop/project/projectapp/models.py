from __future__ import unicode_literals

from django.db import models

class Topping(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=30)


    class Meta:
          ordering = ('created',)

class Pizza(models.Model):
    name = models.CharField(max_length=50)
    toppings = models.ManyToManyField(Topping)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
          ordering = ('created',)

