from rest_framework import serializers
from .models import Blog


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'title', 'description']  # Do not include 'author'
        extra_kwargs = {
            'title': {'required': True, 'allow_blank': False},
            'description': {'required': True},
        }
