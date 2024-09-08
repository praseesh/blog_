from django.db import models
from django.utils import timezone
from user.models import UserInfo

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
    categories = models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'posts'
        ordering = ['-created_at']

    def __str__(self):
        return self.title