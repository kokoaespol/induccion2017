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
            'id','name', 'last_name', 'skin','shirt',
            'hair','genre','ranking','user',
        )
        depth = 1

class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Option
        fields = (
            'id','name','is_answer','puzzle'
        )

class PuzzleSerializer(serializers.ModelSerializer):
    options = serializers.SerializerMethodField()

    class Meta:
        model = Puzzle
        fields = (
            'id','name','description','medal','options',
        )
        depth = 1

    def get_opciones(self, puzzle):
        options = puzzle.options.all()
        serializer = OptionSerializer(options, many=True)
        return serializer.data

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
            'id','name','description','n_puzzle','image','block',
        )
        depth = 1

class TreasureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Treasure
        fields = (
            'id','name','description','image',
        )

class PuzzleTreasureSerializer(serializers.ModelSerializer):
    class Meta:
        model = PuzzleTreasure
        fields = (
            'id','puzzle','treasure',
        )

class PuzzleProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = PuzzleProfile
        fields = (
            'id','is_correct','puzzle','profile',
        )