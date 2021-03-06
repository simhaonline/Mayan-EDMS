from rest_framework import serializers

from .models import DocumentPageContent


class DocumentPageContentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('content',)
        model = DocumentPageContent
