from rest_framework import serializers
from .models import Notes

# ModelSerializer automatically generates fields based on the model.
# id field (primary key) is included to uniquely identify each record.

class NotesSerializers(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%B %d, %Y, %H:%M:%S", read_only=True)
    class Meta:
        model = Notes
        fields = ['id', 'title', 'content', 'created_at']