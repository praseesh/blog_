from django.db import models
from django.utils import timezone
from user.models import UserInfo
from django.db import models
from django.conf import settings

class BlacklistedAccessToken(models.Model):
    token = models.CharField(max_length=255, unique=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    blacklisted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Blacklisted token for user: {self.user}"
    
class Category(models.Model):
    CATEGORY_CHOICES = [
        ('TECH', 'Technology'),
        ('HEALTH', 'Health'),
        ('LIFESTYLE', 'Lifestyle'),
        ('BUSINESS', 'Business'),
        ('TRAVEL', 'Travel'),
        ('EDUCATION', 'Education'),
        ('FOOD', 'Food'),
        ('ENTERTAINMENT', 'Entertainment'),
        ('SPORTS', 'Sports'),
        ('FINANCE', 'Finance'),
        ('ART', 'Art'),
        ('MUSIC', 'Music'),
        ('GAMING', 'Gaming'),
        ('POLITICS', 'Politics'),
        ('SCIENCE', 'Science'),
        ('BOOKS', 'Books'),
        ('PHOTOGRAPHY', 'Photography'),
        ('OTHER','Other')
    ]
    name = models.CharField(max_length=30, choices=CATEGORY_CHOICES, unique=True)
    class Meta:
        db_table = 'category'
        
    def __str__(self):
        return dict(self.CATEGORY_CHOICES).get(self.name)
    
class Posts(models.Model):
    title = models.CharField(max_length=40,null=False,blank=False)
    content = models.TextField(max_length=1000, null=False,blank=False)
    author = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    categories = models.ForeignKey(Category,on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                   related_name='liked_posts', blank=True)  
    def like_count(self):
        return self.likes.count()
    
    class Meta:
        db_table = 'posts'
        ordering = ['-created_at']

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    post = models.ForeignKey(Posts, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'comments'
    def __str__(self):
        return f'Comment by {self.author} on {self.post}'