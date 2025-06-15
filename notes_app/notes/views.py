from django.shortcuts import render
from rest_framework import viewsets
from .serializers import NotesSerializers
from .models import Notes

# Create your views here.

# Specifies which serializer to use to convert Notes model instances to JSON and vice versa.
# serializer_class tells DRF how to serialize/deserialize the Book data.

class NotesViewSet(viewsets.ModelViewSet):
    queryset = Notes.objects.all()
    serializer_class = NotesSerializers