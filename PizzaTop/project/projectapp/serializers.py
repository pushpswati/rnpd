from rest_framework import serializers
from projectapp.models import Topping
from projectapp.models import Pizza

class Toppingserializer(serializers.ModelSerializer):
    class Meta:
        model=Topping
        fields=('created','name')

class Pizzaserializer(serializers.ModelSerializer):
    class Meta:
         model=Pizza
         fields=('created','name','toppings')
