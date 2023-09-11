from django.shortcuts import render
from serializers import PersonSerializer
from rest_framework import viewsets
from .models import Person

# Create your views here.

class PersonViewSet(viewsets.ModelViewSet):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()