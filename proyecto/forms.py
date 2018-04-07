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

class BlockForm(forms.ModelForm):
	class Meta:
		model = Block
		fields = '__all__'

class MisionForm(forms.ModelForm):
	class Meta:
		model = Mision
		fields = '__all__'

class TypeRForm(forms.ModelForm):
	class Meta:
		model = TypeR
		fields = '__all__'

class TypeTForm(forms.ModelForm):
	class Meta:
		model = TypeT
		fields = '__all__'

class KeyRForm(forms.ModelForm):
	class Meta:
		model = KeyR
		fields = '__all__'

class KeyTForm(forms.ModelForm):
	class Meta:
		model = KeyT
		fields = '__all__'

class RoomForm(forms.ModelForm):
	class Meta:
		model = Room
		fields = '__all__'

class MisionProfileForm(forms.ModelForm):
	class Meta:
		model = MisionProfile
		fields = '__all__'
