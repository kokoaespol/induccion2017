from django import forms
from proyecto.models import User,Profile,Acertijo,Tesoro,Medalla,Facultad,Opcion

class UserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = '__all__'

class ProfileForm(forms.ModelForm): # form de profile
	class Meta:
		model =  Profile
		fields = '__all__'# al usar all quiere decir que se escogen todos los atributos.

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
