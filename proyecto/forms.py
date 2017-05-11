from django.contrib.auth.models import User
from django import forms
from proyecto.models import Profile,Acertijo,Tesoro,Medalla,Facultad,Opcion,Edificio

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())
	class Meta:
		model = User
		#fields = '__all__'
		fields = ('username', 'password')

class ProfileForm(forms.ModelForm): # form de profile
	class Meta:
		model =  Profile
		fields = ('name', 'last_name', 'color_piel', 'color_camiseta', 'color_cabello', 'sexo', 'ranking')

class AcertijoForm(forms.ModelForm):
	class Meta:
		model = Acertijo
		fields = '__all__'

class FacultadForm(forms.ModelForm):
	class Meta:
		model = Facultad
		fields = '__all__'

class MedallaForm(forms.ModelForm):
	class Meta:
		model = Medalla
		fields = '__all__'

class TesoroForm(forms.ModelForm):
	class Meta:
		model = Tesoro
		fields = '__all__'

class OpcionForm(forms.ModelForm):
	class Meta:
		model = Opcion
		fields = '__all__'

class EdificioForm(forms.ModelForm):
	class Meta:
		model = Edificio
		fields = '__all__'
