from django.urls import path
from post.views import PostView, PostCreateView  # Use absolute import instead of '.views'

urlpatterns = [
    path('', PostView.as_view(), name="posts"),
    path('create/', PostCreateView.as_view(), name='post-create'),
    
]