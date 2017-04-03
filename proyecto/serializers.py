from rest_framework import serializers
from proyecto.models import User,Profile,Acertijo,Tesoro,Medalla,Facultad

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'first_name','last_name','username',
        )
class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Profile
        fields = (
            'user','color_piel','color_camiseta',
            'color_cabello','sexo','ranking',
        )

class AcertijoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Acertijo
        fields = (
            'titulo','descripcion','respuesta',
        )

class FacultadSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
    class Meta:
        model = Facultad
        fields = (
            'nombre','profile'
        )

class MedallaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medalla
        fields = (
            'titulo','descripcion','n_tesoro',
            'icono',
        )

class TesoroSerializer(serializers.ModelSerializer):
    perfil = ProfileSerializer()
    medalla = MedallaSerializer()
    facultad = FacultadSerializer()
    acertijo = AcertijoSerializer()
    class Meta:
        model = Tesoro
        fields = (
            'nombre','descripcion','icono',
            'perfil','medalla','facultad','acertijo',
        )
