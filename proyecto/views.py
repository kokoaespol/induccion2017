from django.shortcuts import render,render_to_response
from proyecto.models import User,Profile,Acertijo,Tesoro,Medalla,Facultad
from proyecto.forms import UserForm,ProfileForm,AcertijoForm,TesoroForm,MedallaForm,FacultadForm
from django.http import HttpResponseRedirect,HttpResponse
from django.template.context_processors import csrf
# Create your views here.

def home(request):
	entradas = User.objects.all()[:10]
	return render_to_response('pruebaSaves.html', {'users' : entradas})

"""def register(request):
	user_form = UserForm()
	if request.method == 'POST':
		user_form = UserForm(request.POST, prefix = "user")
		if user_form.is_valid():
			user_form.save()
			return HttpResponseRedirect('/saves/')
	args = {}
	args.update(csrf(request))
	args['user_form'] = user_form
	return render_to_response('register.html',args)"""

def generateView(request):
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
        	print("Error")
	args= {}
	args.update(csrf(request))
	args['profile_form'] = profile_form
	args['acertijo_form'] = acertijo_form
	args['facultad_form'] = facultad_form
	args['medalla_form'] = medalla_form
	args['tesoro_form'] = tesoro_form
	return render(request,'register.html',args)
