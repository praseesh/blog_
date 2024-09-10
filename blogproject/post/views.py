from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,generics
from rest_framework_simplejwt.tokens import AccessToken,RefreshToken
from .serializers import PostCreateSerializer, PostViewSerializer, CommentSerializer
from .models import Posts, Comment
from django.db.models import Q
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken
from rest_framework.exceptions import AuthenticationFailed

# class PostView(APIView):
#     authentication_classes = [JWTAuthentication]  
#     permission_classes = [IsAuthenticated]
#     def get(self,request,*args, **kwargs):
#         if not request.user.is_authenticated:
#             return Response({'error':'Authentication Credentials are not provided'},
#                             status=status.HTTP_401_UNAUTHORIZED)
#         else:
#             posts = Posts.objects.all()
#             serializer = PostViewSerializer(posts,many=True)
#             return Response (serializer.data,status=status.HTTP_200_OK)
class PostView(APIView):
    authentication_classes = [JWTAuthentication]  
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        posts = Posts.objects.all()
        serializer = PostViewSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class PostCreateView(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]  
    permission_classes = [IsAuthenticated]
    queryset = Posts.objects.all()
    serializer_class = PostCreateSerializer

class LikePostView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def post(self, request, post_id, *args, **kwargs):
        try:
            post =Posts.objects.get(id=post_id)
        except Posts.DoesNotExist:
            return Response({'error':'Post Not Found'}, status=status.HTTP_404_NOT_FOUND)
        if request.user in post.likes.all():
            post.likes.remove(request.user)  
            return Response({'message': 'Post disliked', 'like_count': post.like_count()}, status=status.HTTP_200_OK)
        else:
            post.likes.add(request.user)  
            return Response({'message': 'Post liked', 'like_count': post.like_count()}, status=status.HTTP_200_OK)

class CommentPostView(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        post_id = self.kwargs.get('post_id')
        post = Posts.objects.get(id=post_id)
        
        serializer.save(post=post, author=self.request.user)
    
