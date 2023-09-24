from rest_framework import serializers
from .models import Image, Post  # Import your Image model


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = "__all__"


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"  # Serialize all fields of the Post model
