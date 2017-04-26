from django.db import models
from django.contrib.auth.models import User
# Create your models here.
SEX = (
    ('H','Hombre'),
    ('M','Mujer'),
)

class Profile(models.Model):
#relaciones
    user = models.OneToOneField( User, on_delete=models.CASCADE)#uno a uno
#atributos
    name = models.CharField(max_length=50, null=True, blank=True)#texto
    last_name = models.CharField(max_length=50, null=True, blank=True)#texto
    email = models.EmailField(max_length=70,blank=True, null=True)
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
#atributos
    titulo = models.CharField(max_length=500)#texto
    descripcion = models.TextField()#textolargo
    respuesta = models.TextField()#textolargo
    respondido = models.BooleanField(default=False)

    def __unicode__(self):
        return self.titulo

    class Meta:
        verbose_name = "Acertijo"
        verbose_name_plural = "Acertijos"

class Facultad(models.Model):
#relaciones
    profile = models.ForeignKey(Profile,default='')#uno a muchos
#atributos
    nombre = models.CharField(max_length=100)#texto

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name = "Facultad"
        verbose_name_plural = "Facultades"

class Medalla(models.Model):
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

class Tesoro(models.Model):
#relaciones
    user = models.ManyToManyField(User)#muchos a muchos
    medalla = models.ForeignKey(Medalla, on_delete=models.CASCADE)#uno a muchos
    facultad = models.ForeignKey(Facultad, on_delete=models.CASCADE)#uno a muchos
    acertijo = models.OneToOneField( Acertijo, on_delete=models.CASCADE)#uno a uno
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
    acertijo = models.ForeignKey(Acertijo,on_delete=models.CASCADE)
    #atributos
    texto = models.TextField()
    correcto = models.BooleanField(default=False)

    def __unicode__(self):
        return self.texto

    class Meta:
        verbose_name = "Opcion"
        verbose_name_plural = "Opciones"
#A
