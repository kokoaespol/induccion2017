from proyecto.serializers import UserSerializer,ProfileSerializer,AcertijoSerializer,TesoroSerializer,MedallaSerializer,FacultadSerializer,OpcionSerializer
from proyecto.forms import UserForm,ProfileForm,AcertijoForm,TesoroForm,MedallaForm,FacultadForm,OpcionForm
from proyecto.models import User,Profile,Acertijo,Tesoro,Medalla,Facultad,Opcion
from django.views.decorators.csrf import csrf_exempt
from django.template.context_processors import csrf
from django.http import HttpResponse, JsonResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import viewsets
from django.contrib.auth.models import User
# Create your views here.


class AcertijoViewSet(viewsets.ModelViewSet):
    queryset = Acertijo.objects.all()
    serializer_class = AcertijoSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TesoroViewSet(viewsets.ModelViewSet):
    queryset = Tesoro.objects.all()
    serializer_class = TesoroSerializer

class MedallaViewSet(viewsets.ModelViewSet):
    queryset = Medalla.objects.all()
    serializer_class = MedallaSerializer

class OpcionViewSet(viewsets.ModelViewSet):
    queryset = Opcion.objects.all()
    serializer_class = OpcionSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


def savePost(request):
    user_form = UserForm()
    profile_form = ProfileForm()
    acertijo_form = AcertijoForm()
    facultad_form = FacultadForm()
    medalla_form = MedallaForm()
    tesoro_form = TesoroForm()
    opcion_form = OpcionForm()
    if request.method == 'POST':
        user_form = UserForm(request.POST,prefix="user")
        profile_form = ProfileForm(request.POST, prefix = "profile")
        acertijo_form = AcertijoForm(request.POST, prefix = "acertijo")
        facultad_form = FacultadForm(request.POST, prefix = "facultad")
        medalla_form = MedallaForm(request.POST, prefix = "medalla")
        tesoro_form = TesoroForm(request.POST, prefix = "tesoro")
        opcion_form = OpcionForm(request.POST, prefix = "opcion")
        if profile_form.is_valid() and acertijo_form.is_valid() and facultad_form.is_valid() and medalla_form.is_valid() and tesoro_form.is_valid() and opcion_form.is_valid():
            profile_form.save()
            acertijo_form.save()
            facultad_form.save()
            medalla_form.cleaned_data["medalla"]
            medalla_form.save()
            tesoro_form.cleaned_data["tesoro"]
            tesoro_form.save()
            opcion_form.save()
        else:
            return HttpResponse(status=500)
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=400)
