from rest_framework import serializers
from .models import Notes

# ModelSerializer automatically generates fields based on the model.
# id field (primary key) is included to uniquely identify each record.

class NotesSerializers(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%B %d, %Y, %H:%M:%S", read_only=True)
    
    class Meta:
        model = Notes
        fields = ['id', 'title', 'content', 'created_at']

    # validate content length
    def validate(self, data):
        title = data.get('title', '')
        content = data.get('content', '')

        if len(title) > 100:
            raise serializers.ValidationError("Title cannot exceed 100 characters")
        if len(content) > 1000:
            raise serializers.ValidationError("Content cannot exceed 1000 characters")
        
        return data