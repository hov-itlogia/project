from django.shortcuts import render # ete ches ogtagorcum jnji faylic mi tox
from rest_framework import viewsets

from books.models import Service
from books.serializers import ServiceSerializer


# Create your views here.

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
