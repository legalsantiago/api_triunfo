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
                  'Position_company',
                  'document_id',
                  'password']
        
    def create(self, validated_data):
        user = User(
        username=validated_data['username'],
        name = validated_data['name'],
        last_name = validated_data['last_name'],
        email=validated_data['email'],
        Position_company=validated_data['Position_company'],
        document_id=validated_data['document_id']
        ) 
        #user = User(**validated_data)  OTRA MANERA DE UTILIZARLO
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
                  'document_id']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class serializerPassword(serializers.Serializer):
    currently_password = serializers.CharField(max_length=20, min_length=6, write_only=True)
    new_password = serializers.CharField(max_length=20, min_length=6, write_only=True)

    # def validate(self,data):
    #     if data['currently_password'] == data['new_password'] :
    #         raise serializers.ValidationError({
    #             'message':'ambas contraseñas son iguales',
    #             'password':data['new_password']
    #         })
    #     return data
    
    def validate(self,data):
        if data.get('currently_password') == data.get('new_password'):
            raise serializers.ValidationError({
                'descript':'ambas contraseñas son iguales',
                'password':data.get('new_password')
            })
        return data
        



    