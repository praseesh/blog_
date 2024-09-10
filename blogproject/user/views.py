from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserInfoSerializer,UserLoginSerializer
from rest_framework import status,generics
from rest_framework_simplejwt.tokens import RefreshToken,AccessToken
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import GenericAPIView
from django.utils import timezone
from rest_framework_simplejwt.authentication import JWTAuthentication


User=get_user_model()

class UserRegistrationViews(APIView):
    def post(self,request, *args, **kwargs):
        serializer = UserInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'User Registration Successful'},status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
class UserLoginView(APIView):
    serializer_class = UserLoginSerializer
    def post(self,request, *args, **kwargs):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.validated_data['user']
            refresh = RefreshToken.for_user(user)
            access = str(refresh.access_token)
            
            response_data = {
                'access token': access,
                'refresh': str(refresh),
                'user' :{
                    'id': user.id,
                    'username': user.username,
                    'email': user.email,
                    'phone number': user.phone,
                }
            }
            return Response(response_data,status=status.HTTP_200_OK)

class LogoutView(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request, *args, **kwargs):
        print("1")
        
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"success": "User logged out successfully"},  status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
class UserListView(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]  
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserInfoSerializer
    
class UserDetailView(generics.RetrieveAPIView):
    authentication_classes = [JWTAuthentication]  # These should be class attributes
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()  # Define the queryset at the class level
    serializer_class = UserInfoSerializer
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)