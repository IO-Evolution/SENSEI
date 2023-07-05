from rest_framework import serializers

from .models import FSE_DOCUMENT

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = FSE_DOCUMENT
        fields = ["id", "doc_type", "data", "status", "xml_file", "xml_code"]