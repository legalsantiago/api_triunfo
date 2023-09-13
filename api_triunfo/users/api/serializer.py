from rest_framework import serializers
from api_triunfo.users.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

#serializado para jwt
class CustonTokenObtainPairSerializer(TokenObtainPairSerializer):
    pass

#SERALIZADOR PARA LA CREACION DE USUARIOS BASE
class UserSerializerCreate(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username',
                  'name',
                  'last_name',
                  'email',
                  'cargo',
                  'document_id',
                  'password']
        
    def create(self, validated_data):
        user = User(
        username=validated_data['username'],
        name = validated_data['name'],
        last_name = validated_data['last_name'],
        email=validated_data['email'],
        cargo=validated_data['cargo'],
        document_id=validated_data['document_id']
        ) 
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    def update(self, instance, validated_data):
        update_user = super().update(instance, validated_data)
        update_user.set_password(validated_data['password'])
        update_user.save()
        return update_user

#SERIALIZADOR ESTANDAR 
class UserSerializerBase(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id',
                  'username',
                  'name',
                  'last_name',
                  'document_id',
                  'email',
                  'cargo',
                  'is_active']
        

    def to_representation(self, instance):
        return {
            'Id':instance.id,
            'Username': instance.username,
            'Nombre': instance.name,
            'Email': instance.email,
            'Apellidos': instance.last_name,
        }


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

