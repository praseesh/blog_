from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserInfoSerializer,UserLoginSerializer
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model

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
            print("@@@@@@@@@",user)
            refresh = RefreshToken.for_user(user)
            print("$$$$$$$$$$$")
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

class LogoutView(APIView):
    def post(self,request,*args, **kwargs):
        try:
            refresh_token = request.data['refresh']
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({'detail':'logout successful'}, status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            print("$$$$$$$$$$$",e)
            return Response({'detailssss':'invalid token'}, status=status.HTTP_400_BAD_REQUEST)