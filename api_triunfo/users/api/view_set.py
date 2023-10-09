from rest_framework.viewsets import GenericViewSet
#from django.contrib.auth.models import Group
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework.decorators import action
from api_triunfo.users.api.serializer import UserSerializerBase,UserSerializerCreate, serializerPassword
from rest_framework import status
from api_triunfo.users.models import User

class UserAPIview(GenericViewSet):
    
    serializer_class_create = UserSerializerCreate
    serializer_class= UserSerializerBase
    queryset = None
    modelo = User

    def get_object(self, pk=None):
        try:
            obj = self.serializer_class.Meta.model.objects.filter(id = pk, is_active=True)
            return obj
        except:
            raise print("error not found 404")


    def get_queryset(self):
        if self.queryset is None:
            self.queryset = self.serializer_class().Meta.model.objects.filter(is_active = True).values('id',
                                                                                                       'username',
                                                                                                       'name',
                                                                                                       'document_id')
            return self.queryset
        else: 
            return self.queryset
        
         
    #actualizar contraseña
    @swagger_auto_schema(
        request_body = serializerPassword,  # Define el serializador para la solicitud
        responses = {200: serializerPassword}  # Define el serializador para la respuesta
    )
    @action(detail=True, methods=['post'], url_path='update_password')
    def change_password(self,request,pk=None):
        user = self.modelo.objects.get(id = pk)
        serializer_password = serializerPassword(data = request.data)  

        if serializer_password.is_valid():
            new_password = serializer_password.validated_data.get('new_password')
            print(new_password)
            user.set_password(new_password)
            user.save()
            return Response({'message':'contraseña actualizada',},status=status.HTTP_200_OK)
        else: 
            return Response({
                'message':'errores en la data recibida' ,
                'errors':serializer_password.errors
            }, status=status.HTTP_400_BAD_REQUEST)
    
    
    def list(self, request):
        users = self.get_queryset()
        users_serializados = self.serializer_class(users,many=True)
        return Response(users_serializados.data, status=status.HTTP_200_OK)
    
    
    @swagger_auto_schema(
        request_body = serializer_class_create,  # Define el serializador para la solicitud
        responses = {200: serializer_class_create}  # Define el serializador para la respuesta
    )
    def create(self, request):
        serializer_user = self.serializer_class_create(data=request.data)

        if serializer_user.is_valid():
            serializer_user.save()
            return Response({'message':'Usuario creado con exito'},status= status.HTTP_201_CREATED)
        else:   
            return Response(serializer_user.errors,status=status.HTTP_400_BAD_REQUEST)
        
    
    def retrieve(self, request, pk=None):
        user = self.modelo.objects.get(id = pk)
        if user.is_active:
            serializer = self.serializer_class(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"message": "El usuario no existe"}, status=status.HTTP_404_NOT_FOUND)
        

    @swagger_auto_schema(
        request_body= serializer_class_create,  # Define el serializador para la solicitud
        responses={201: serializer_class_create}  # Define el serializador para la respuesta
    )
    def update(self, request, pk=None):
        """
         debe enviarse los datos que se solicitan 
        """
        try:
            user = self.modelo.objects.get(id=pk)
            if user:
                serializer_user = self.serializer_class_create(user, data=request.data)
                if serializer_user.is_valid():
                    serializer_user.save()
                    return Response({'message':'Usuario Actualizado'},status=status.HTTP_200_OK)
                else: 
                    return Response({'message':'','error':serializer_user.errors}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'message':'no se encontro Usuario'}, status=status.HTTP_404_NOT_FOUND)

            
    def destroy(self, request, pk=None):
        user = self.modelo.objects.get(id=pk)

        if user:
            user.is_active = False
            user.save()
            return Response({'message':'Usuario Eliminado'},status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'message':'Usuario no encontrado'},status=status.HTTP_404_NOT_FOUND)
        

        

