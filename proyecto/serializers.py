from rest_framework import serializers
from proyecto.models import Profile,Acertijo,Tesoro,Medalla,Facultad,Opcion
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 'username', 'email', 'password',
        )

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = (
            'id','user','name', 'last_name', 'color_piel','color_camiseta',
            'color_cabello','sexo','ranking',
        )

class OpcionSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Opcion
        fields = (
            'id','acertijo','texto','correcto',
        )

class AcertijoSerializer(serializers.ModelSerializer):
    opciones = serializers.SerializerMethodField()

    class Meta:
        model = Acertijo
        fields = (
            'id','titulo','descripcion','respuesta','respondido', 'opciones'
        )

    def get_opciones(self, acertijo):
        opciones = acertijo.opciones.all()
        serializer = OpcionSerializer(opciones, many=True)
        return serializer.data

class FacultadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Facultad
        fields = (
            'id','nombre','profile',
        )

class MedallaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medalla
        fields = (
            'id','titulo','descripcion','n_tesoro',
            'icono','facultad',
        )
        depth = 1

class TesoroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tesoro
        fields = (
            'id','nombre','descripcion','icono',
            'user','medalla','facultad','acertijo',
        )
        depth = 2