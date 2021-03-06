#from proyecto.serializers import UserSerializer,ProfileSerializer,AcertijoSerializer,TesoroSerializer,MedallaSerializer,FacultadSerializer,OpcionSerializer,EdificioSerializer
from proyecto.serializers import *
from proyecto.forms import *#UserForm,ProfileForm,AcertijoForm,TesoroForm,MedallaForm,FacultadForm,OpcionForm,EdificioForm
from proyecto.models import *#User,Profile,Acertijo,Tesoro,Medalla,Facultad,Opcion,Edificio
from django.views.decorators.csrf import csrf_exempt
from django.template.context_processors import csrf
from django.http import HttpResponse, JsonResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.template import RequestContext
from django.shortcuts import render_to_response
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.


class MisionViewSet(viewsets.ModelViewSet):
    queryset = Mision.objects.all()
    serializer_class = MisionSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('id',)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TreasureViewSet(viewsets.ModelViewSet):
    queryset = Treasure.objects.all()
    serializer_class = TreasureSerializer
    permission_classes = (IsAuthenticated,)

class MedalViewSet(viewsets.ModelViewSet):
    queryset = Medal.objects.all()
    serializer_class = MedalSerializer
    permission_classes = (IsAuthenticated,)

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (IsAuthenticated,)

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('name',)

class BlockViewSet(viewsets.ModelViewSet):
    queryset = Block.objects.all()
    serializer_class = BlockSerializer
    permission_classes = (IsAuthenticated,)

class MisionProfileViewSet(viewsets.ModelViewSet):
    queryset = MisionProfile.objects.all()
    serializer_class = MisionProfileSerializer
    permission_classes = (IsAuthenticated,)


class TypeRViewSet(viewsets.ModelViewSet):
    queryset = TypeR.objects.all()
    serializer_class = TypeRSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (DjangoFilterBackend,)
    #filter_fields = ('name',)


class TypeTViewSet(viewsets.ModelViewSet):
    queryset = TypeT.objects.all()
    serializer_class = TypeTSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (DjangoFilterBackend,)
    #filter_fields = ('name',)

class KeyRViewSet(viewsets.ModelViewSet):
    queryset = KeyR.objects.all()
    serializer_class = KeyRSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (DjangoFilterBackend,)
    #filter_fields = ('name',)

class KeyTViewSet(viewsets.ModelViewSet):
    queryset = KeyT.objects.all()
    serializer_class = KeyTSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (DjangoFilterBackend,)
    #filter_fields = ('name',)

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (DjangoFilterBackend,)
    #filter_fields = ('name',)






@csrf_exempt
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


@csrf_exempt
def register(request):
    # Like before, get the request's context.
    context = RequestContext(request)

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and ProfileForm.
        user_form = UserForm(data=request.POST)
        profile_form = ProfileForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user

            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the UserProfile model.
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            # Now we save the UserProfile model instance.
            profile.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print(user_form.errors, profile_form.errors)

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        profile_form = ProfileForm()

    # Render the template depending on the context.
    return render_to_response(
            'register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered},
            context)


def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'user': UserSerializer(user, context={'request': request}).data
    }
