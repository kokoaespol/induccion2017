from proyecto.serializers import UserSerializer,ProfileSerializer,AcertijoSerializer,TesoroSerializer,MedallaSerializer,FacultadSerializer
from proyecto.forms import UserForm,ProfileForm,AcertijoForm,TesoroForm,MedallaForm,FacultadForm
from proyecto.models import User,Profile,Acertijo,Tesoro,Medalla,Facultad
from django.views.decorators.csrf import csrf_exempt
from django.template.context_processors import csrf
from django.http import HttpResponse, JsonResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse
# Create your views here.

@csrf_exempt#user
def user_list(request):
    if request.method == 'GET':
        usuario = User.objects.all()
        userserializer = UserSerializer(usuario, many=True)
        return JsonResponse(userserializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt#facultad
def facultad_list(request):
    if request.method == 'GET':
        facultad = Facultad.objects.all()
        facultadserializer = FacultadSerializer(facultad, many=True)
        return JsonResponse(facultadserializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = FacultadSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt#medalla
def medalla_list(request):
    if request.method == 'GET':
        medalla = Medalla.objects.all()
        medallaserializer = MedallaSerializer(medalla, many=True)
        return JsonResponse(medallaserializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MedallaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt#tesoro
def tesoro_list(request):
    if request.method == 'GET':
        tesoro = Tesoro.objects.all()
        tesoroserializer = TesoroSerializer(tesoro, many=True)
        return JsonResponse(tesoroserializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TesoroSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt#profile
def profile_list(request):
    if request.method == 'GET':
        perfil = Profile.objects.all()
        profileserializer = ProfileSerializer(perfil, many=True)
        return JsonResponse(profileserializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProfileSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt#acertijo
def acertijo_list(request):
    if request.method == 'GET':
        acertijo = Acertijo.objects.all()
        acertijoserializer = AcertijoSerializer(acertijo, many=True)
        return JsonResponse(acertijoserializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AcertijoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

"""def savePost(request):
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
        	medalla_fofrom django.http import HttpResponserm.cleaned_data["medalla"]
        	medalla_form.save()
        	tesoro_form.cleaned_data["tesoro"]
        	tesoro_form.save()
        else:
        	return HttpResponse(status=500)
		return HttpResponse(status=200)
	else:
		return HttpResponse(status=400)"""
