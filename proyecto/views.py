from proyecto.models import User,Profile,Acertijo,Tesoro,Medalla,Facultad
from proyecto.forms import UserForm,ProfileForm,AcertijoForm,TesoroForm,MedallaForm,FacultadForm
from django.http import HttpResponse
from django.template.context_processors import csrf
# Create your views here.

def savePost(request):
	user_form = UserForm()
	profile_form = ProfileForm()
	acertijo_form = AcertijoForm()
	facultad_form = FacultadForm()
	medalla_form = MedallaForm()
	tesoro_form = TesoroForm()

	if request.method == 'POST':
		user_form = UserForm(request.POST,prefix="user")
		profile_form = ProfileForm(request.POST, prefix = "profile")
        acertijo_form = AcertijoForm(request.POST, prefix = "acertijo")
        facultad_form = FacultadForm(request.POST, prefix = "facultad")
        medalla_form = MedallaForm(request.POST, prefix = "medalla")
        tesoro_form = TesoroForm(request.POST, prefix = "tesoro")

        if profile_form.is_valid() and acertijo_form.is_valid() and facultad_form.is_valid() and medalla_form.is_valid() and tesoro_form.is_valid():
        	profile_form.save()
        	acertijo_form.save()
        	facultad_form.save()
        	medalla_form.cleaned_data["medalla"]
        	medalla_form.save()
        	tesoro_form.cleaned_data["tesoro"]
        	tesoro_form.save()
        else:
        	return HttpResponse(status=500)
		return HttpResponse(status=200)
	else:
		return HttpResponse(status=400)
