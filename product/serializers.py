from rest_framework import serializers
from .models import Ratting,Comment

class RattingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ratting
        fields = ['user', 'product', 'rating']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['user', 'product', 'comment']