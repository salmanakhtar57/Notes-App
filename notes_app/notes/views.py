from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import NotesSerializers
from .models import Notes

# Create your views here.

# Specifies which serializer to use to convert Notes model instances to JSON and vice versa.
# serializer_class tells DRF how to serialize/deserialize the Book data.

# class NotesViewSet(viewsets.ModelViewSet):
#     queryset = Notes.objects.all()
#     serializer_class = NotesSerializers


# Get all notes

@api_view(['GET', 'POST'])
def notes_list_create(request):
    if request.method == 'GET':
        notes = Notes.objects.all().order_by('-created_at')
        serializer = NotesSerializers(notes, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = NotesSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
def notes_detail(request, pk):
    try:
        note = Notes.objects.get(pk=pk)
    except Notes.DoesNotExist:
        return Response({'error': 'Note not found'}, status=status.HTTP_404_NOT_FOUND)
    
    # get a sinle note
    if request.method == 'GET':
        serializer = NotesSerializers(note)
        return Response(serializer.data)
    
    # update a note
    elif request.method == 'PUT':
        serializer = NotesSerializers(note, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # delete a note(s)
    elif request.method == "DELETE":
        note.delete()
        return Response({'message': "Note deleted successfully!"})