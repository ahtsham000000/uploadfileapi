from rest_framework import serializers
from .models import FileUpload

class FileUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileUpload
        fields = ('file', 'file_url')
        read_only_fields = ('file_url',)

    def validate_file(self, value):
        # Check file type
        if not value.name.endswith(('.jpg', '.jpeg', '.png', '.csv')):
            raise serializers.ValidationError("Only .jpg, .jpeg, .png, and .csv files are allowed.")
        return value
