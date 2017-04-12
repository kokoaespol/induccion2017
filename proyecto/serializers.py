from rest_framework import serializers
from proyecto.models import User,Profile,Acertijo,Tesoro,Medalla,Facultad,Opcion

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id','first_name','last_name','username',
        )

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = (
            'id','user','color_piel','color_camiseta',
            'color_cabello','sexo','ranking',
        )

class AcertijoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Acertijo
        fields = (
            'id','titulo','descripcion','respuesta','respondido',
        )

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
            'icono',
        )

class TesoroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tesoro
        fields = (
            'id','nombre','descripcion','icono',
            'user','medalla','facultad','acertijo',
        )

class OpcionSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Opcion
        fields = (
            'id','acertijo','texto','correcto',
        )
