from rest_framework import serializers 
from .models import Post , Comment
from django.contrib.auth import get_user_model
User = get_user_model()
class PostSerializer(serializers.ModelSerialiazer):
    author = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Post 
        fields = ['id','title', 'content','created_at','updated_at','author']
        read_only_fields = ['id', 'author', 'created_at', 'updated_at']

class CommentSerializer(serializers.ModelSerializer):
     author = serializers.StringRelatedField(read_only=True)
     post = serializers.PrimaryKeyRelatedField(read_only=True)
     class Meta:
        model = Comment 
        fields = ['id','content','created_at','updated_at','post','author']
        read_only_fields = ['id', 'author', 'post', 'created_at', 'updated_at']
