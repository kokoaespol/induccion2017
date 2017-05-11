from rest_framework import serializers
from proyecto.models import Profile,Acertijo,Tesoro,Medalla,Facultad,Opcion,Edificio
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 'username', 'password',
        )

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = (
            'id','name', 'last_name', 'color_piel','color_camiseta',
            'color_cabello','sexo','ranking','user','medalla','facultad',
            'edificio',
        )
        depth = 1

class OpcionSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Opcion
        fields = (
            'id','texto','correcto','acertijo',
        )

class AcertijoSerializer(serializers.ModelSerializer):
    opciones = serializers.SerializerMethodField()

    class Meta:
        model = Acertijo
        fields = (
            'id','titulo','descripcion','respuesta','respondido', 'correcto',
            'medalla', 'opciones',
        )
        depth = 1

    def get_opciones(self, acertijo):
        opciones = acertijo.opciones.all()
        serializer = OpcionSerializer(opciones, many=True)
        return serializer.data

class FacultadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Facultad
        fields = (
            'id','nombre',
        )

class EdificioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Edificio
        fields = (
            'id','nombre','facultad',
        )

class MedallaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medalla
        fields = (
            'id','titulo','descripcion','n_tesoro','icono',
        )
        depth = 1

class TesoroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tesoro
        fields = (
            'id','nombre','descripcion','icono','acertijo',
        )
        depth = 2