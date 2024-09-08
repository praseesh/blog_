from django.urls import path
from post.views import PostView  # Use absolute import instead of '.views'

urlpatterns = [
    path('', PostView.as_view(), name="posts"),
]