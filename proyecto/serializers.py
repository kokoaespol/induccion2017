from rest_framework import serializers
from .models import *
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
            'id','name', 'last_name', 'skin',
            'genre','ranking','user',
        )
        depth = 1

class MisionSerializer(serializers.ModelSerializer):
    #options = serializers.SerializerMethodField()

    class Meta:
        model = Mision
        fields = (
            'id','name','description','mision',
        )
        depth = 1
    '''
    def get_options(self, puzzle):
        options = puzzle.options.all()
        serializer = OptionSerializer(options, many=True)
        return serializer.data
    '''

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = (
            'id','name',
        )

class BlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Block
        fields = (
            'id','name','department',
        )

class MedalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medal
        fields = (
            'id','name','description','n_puzzle','image',
        )
        depth = 1

class TreasureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Treasure
        fields = (
            'id','name','description','image',
            'room','keyT','mision',
        )

class MisionProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = MisionProfile
        fields = (
            'id','name','description','is_correct',
            'mision','profile',
        )


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = (
            'id','name','description','block','keyR',
        )


class TypeRSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeR
        fields = (
            'id','name','description',
        )

class TypeTSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeT
        fields = (
            'id','name','description',
        )

class KeyRSerializer(serializers.ModelSerializer):
    class Meta:
        model = KeyR
        fields = (
            'id','name','description','posX','posY','typeR',
        )


class KeyTSerializer(serializers.ModelSerializer):
    class Meta:
        model = KeyT
        fields = (
            'id','name','description','posX','posY','typeT',
        )

