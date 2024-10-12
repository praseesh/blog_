from django.urls import path
from post.views import PostView, PostCreateView,LikePostView, CommentPostView,UserPostView

urlpatterns = [
    path('', PostView.as_view(), name="posts"),
    path('create/', PostCreateView.as_view(), name='post-create'),
    path('<int:post_id>/like/', LikePostView.as_view(), name='like-post'),
    path('<int:post_id>/comment/', CommentPostView.as_view(), name='comment-post'),
    path('<int:post_id>/post/',UserPostView.as_view(), name="user-post"),

]