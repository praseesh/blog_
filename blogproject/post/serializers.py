from rest_framework import serializers
from .models import Posts, Category
from user.models import UserInfo

# class CategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = ['id', 'name']
        
class PostViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = '__all__'