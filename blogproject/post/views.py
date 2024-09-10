from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,generics
from rest_framework_simplejwt.tokens import AccessToken,RefreshToken
from .serializers import PostCreateSerializer, PostViewSerializer
from .models import Posts
from django.db.models import Q
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken
from rest_framework.exceptions import AuthenticationFailed

class PostView(APIView):
    authentication_classes = [JWTAuthentication]  
    permission_classes = [IsAuthenticated]
    def get(self,request,*args, **kwargs):
        if not request.user.is_authenticated:
            return Response({'error':'Authentication Credentials are not provided'},
                            status=status.HTTP_401_UNAUTHORIZED)
        else:
            posts = Posts.objects.all()
            serializer = PostViewSerializer(posts,many=True)
            return Response (serializer.data,status=status.HTTP_200_OK)
    
class PostCreateView(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]  
    permission_classes = [IsAuthenticated]
    queryset = Posts.objects.all()
    serializer_class = PostCreateSerializer
    


    
