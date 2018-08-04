from django.shortcuts import render

from projectapp.models import Topping
from projectapp.serializer import ToppingSerializer

from projectapp.serializer import Pizzaserializer
from django.http import Http404
from projectapp.models import Pizza
from projectapp.models import Topping
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class ToppingView(APIView):
    def __str__(self):
        return "%s (%s)" % (
            self.name,
            ", ".join(topping.name for topping in self.toppings.all()),
        )


