from django.contrib.auth.models import User
from django import forms
from proyecto.models import *#Profile,Acertijo,Tesoro,Medalla,Facultad,Opcion,Edificio

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())
	class Meta:
		model = User
		#fields = '__all__'
		fields = ('username', 'password')

class ProfileForm(forms.ModelForm): # form de profile
	class Meta:
		model =  Profile
		fields = ('name', 'last_name', 'skin', 'shirt', 'hair', 'genre', 'ranking')

class PuzzleForm(forms.ModelForm):
	class Meta:
		model = Puzzle
		fields = '__all__'

class DepartmentForm(forms.ModelForm):
	class Meta:
		model = Department
		fields = '__all__'

class MedalForm(forms.ModelForm):
	class Meta:
		model = Medal
		fields = '__all__'

class TreasureForm(forms.ModelForm):
	class Meta:
		model = Treasure
		fields = '__all__'

class OptionForm(forms.ModelForm):
	class Meta:
		model = Option
		fields = '__all__'

class BlockForm(forms.ModelForm):
	class Meta:
		model = Block
		fields = '__all__'
