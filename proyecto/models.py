from django.db import models
from django.contrib.auth.models import User
# Create your models here.
SEX = (
    ('H','Hombre'),
    ('M','Mujer'),
)

class Facultad(models.Model):
#atributos
    nombre = models.CharField(max_length=100)#texto

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name = "Facultad"
        verbose_name_plural = "Facultades"


class Edificio(models.Model):
    nombre = models.CharField(max_length=100)#texto
#relaciones
    facultad = models.ForeignKey(Facultad,default='', related_name='facultad')#uno a muchos
    
    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name = "Edificio"
        verbose_name_plural = "Edificios"

class Medalla(models.Model):
#relaciones
    #facultad = models.ForeignKey(Facultad,default='', related_name='facultades')#uno a muchos
    #profile = models.ManyToManyField(Profile, null=True, blank=True)#muchos a muchos
#atributos
    titulo = models.CharField(max_length=50)#texto
    descripcion = models.TextField()#textolargo
    n_tesoro = models.IntegerField()#entero
    icono = models.CharField(max_length=50)#imagen
    #icono = models.ImageField(upload_to = '../image/', default = 'pic_folder/None/no-img.jpg')#imagen crear carpeta de default

    def __unicode__(self):
        return self.titulo

    class Meta:
        verbose_name = "Medalla"
        verbose_name_plural = "Medallas"


class Profile(models.Model):
#relaciones
    user = models.OneToOneField( User, on_delete=models.CASCADE, related_name='user')#uno a uno
    medalla = models.ManyToManyField(Medalla, null=True, blank=True)#muchos a muchos
    facultad = models.ForeignKey(Facultad ,default='', related_name='facultades', null=True, blank=True)#uno a muchos
    edificio = models.ForeignKey(Edificio ,default='', related_name='edificios', null=True, blank=True)#uno a muchos
#atributos
    name = models.CharField(max_length=50, null=True, blank=True)#texto
    last_name = models.CharField(max_length=50, null=True, blank=True)#texto
    color_piel = models.CharField(max_length=10,default='#FFFFFF', null=True, blank=True)#texto
    color_camiseta = models.CharField(max_length=10,default='#FFFFFF', null=True, blank=True)#texto
    color_cabello = models.CharField(max_length=10,default='#FFFFFF', null=True, blank=True)#texto
    sexo = models.CharField(max_length=3,choices=SEX,default='H', null=True, blank=True)#texto
    ranking = models.IntegerField(default=0, null=True, blank=True)#entero

    def __unicode__(self):
        return unicode(self.user.username) #para que tenga nombre

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"



class Acertijo(models.Model):
#relaciones
    medalla = models.ForeignKey(Medalla ,default='', related_name='medallas')#uno a muchos
#atributos
    titulo = models.CharField(max_length=500)#texto
    descripcion = models.TextField()#textolargo
    respuesta = models.TextField()#textolargo
    respondido = models.BooleanField(default=False)
    correcto = models.BooleanField(default=False)

    def __unicode__(self):
        return self.titulo

    class Meta:
        verbose_name = "Acertijo"
        verbose_name_plural = "Acertijos"

class Tesoro(models.Model):
#relaciones
    acertijo = models.ForeignKey( Acertijo, null=True, blank=True, related_name='acertijos')#uno a uno
#atributos
    nombre = models.CharField(max_length=50)#texto
    descripcion = models.TextField()#textolargo
    icono = models.CharField(max_length=50)#imagen

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name = "Tesoro"
        verbose_name_plural = "Tesoros"

class Opcion(models.Model):
#relaciones
    acertijo = models.ForeignKey(Acertijo,on_delete=models.CASCADE, related_name='opciones')
#atributos
    texto = models.TextField()
    correcto = models.BooleanField(default=False)

    def __unicode__(self):
        return self.texto

    class Meta:
        verbose_name = "Opcion"
        verbose_name_plural = "Opciones"
#A
