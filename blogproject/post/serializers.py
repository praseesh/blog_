from rest_framework import serializers
from .models import Posts, Category
from user.models import UserInfo
        
class PostViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = '__all__'
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class PostCreateSerializer(serializers.ModelSerializer):
    category_name = serializers.ChoiceField(choices=Category.CATEGORY_CHOICES, write_only=True)

    class Meta:
        model = Posts
        fields = ['title', 'content', 'category_name']

    def create(self, validated_data):
        user = self.context['request'].user
        category_name = validated_data.pop('category_name')
        category, _ = Category.objects.get_or_create(name=category_name)
        post = Posts.objects.create(author=user, categories=category, **validated_data)
        return post