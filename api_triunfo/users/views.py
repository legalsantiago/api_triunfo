from django.contrib.auth import authenticate
from api_triunfo.users.models import User
from rest_framework.request import Request
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from api_triunfo.users.api.serializer import CustonTokenObtainPairSerializer, UserSerializerBase


class login(TokenObtainPairView):
    serializer_class = CustonTokenObtainPairSerializer

    def post(self, request: Request, *args, **kwargs):
        username = request.data.get('username','')
        password = request.data.get('password','')
        user = authenticate(
            username = username,
            password = password
        )

        if user:
            login_serializer = self.serializer_class(data = request.data)
            if login_serializer.is_valid():
                user_serializer = UserSerializerBase(user)

                return Response ({
                    'token':login_serializer.validated_data.get('access'),
                    'refresh-token':login_serializer.validated_data.get('refresh'),
                    'user': user_serializer.data,
                    'message':'inicio de sesion existoso'
                }, status=status.HTTP_200_OK) 
            
            return Response({'error':'contraseña o noombre de usuario incorrectos'}, status=status.HTTP_400_BAD_REQUEST)     
        else:
            return Response({'error':'no existen coincidencias de usuario'}, status=status.HTTP_400_BAD_REQUEST)    

class logout(GenericAPIView):

    def post(self,request,*args, **kwargs):
        
        user_id = request.data.get('user')
        print(user_id)
        user = User.objects.filter(id=user_id).first()
        print(user)
        if user:
            RefreshToken.for_user(user)
            return Response({'message':'sesion cerrada, hasta pronto',},status=status.HTTP_200_OK)
        else:
            return Response({'error':'No existe usuario'},status=status.HTTP_400_BAD_REQUEST)
        

        
    
