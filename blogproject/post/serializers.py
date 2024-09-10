from rest_framework import serializers
from .models import Posts, Category,Comment
from user.models import UserInfo
from django.contrib.auth import get_user_model

User = get_user_model()
        
# class PostViewSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Posts
#         fields = '__all__'
        
# class CategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = ['id', 'name']



class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']  # Display the ID and username of the author

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']
        
class CommentSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())  # Automatically set the author to the current user
    
    class Meta:
        model = Comment
        fields = ['id', 'content', 'author', 'created_at']  # Removed 'post' since it is passed via URL

    def create(self, validated_data):
        content = validated_data.get('content')
        author = self.context['request'].user  # Get the author from the request context
        comment = Comment.objects.create(**validated_data)
        return comment
        
class PostViewSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)  
    categories = CategorySerializer(read_only=True)  
    like_count = serializers.SerializerMethodField()
    liked_by = serializers.SerializerMethodField()
    comment_count = serializers.SerializerMethodField()
    commented_by = serializers.SerializerMethodField()
    comments = CommentSerializer(many=True, read_only=True)  

    class Meta:
        model = Posts
        fields = [
            'id', 'title', 'content', 'author', 'categories','like_count', 'liked_by',
            'comment_count', 'commented_by', 'comments', 'created_at', 'updated_at']

    def get_comment_count(self, obj):
        return obj.comments.count()

    def get_commented_by(self, obj):
        return obj.comments.values_list('author__username', flat=True)
    
    def get_like_count(self, obj):
        return obj.likes.count()

    def get_liked_by(self, obj):
        return obj.likes.values_list('username', flat=True)

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
    
