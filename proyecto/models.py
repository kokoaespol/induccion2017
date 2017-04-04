from django.db import models

# Create your models here.
SEX = (
    ('H','Hombre'),
    ('M','Mujer'),
)
#clases
class User(models.Model):
#atributos
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    username = models.CharField(max_length=10)

    def __unicode__(self):
        return self.username

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

class Profile(models.Model):
#relaciones
    user = models.OneToOneField( User, on_delete=models.CASCADE)#uno a uno
#atributos
    color_piel = models.CharField(max_length=10,default='#FFFFFF')#texto
    color_camiseta = models.CharField(max_length=10,default='#FFFFFF')#texto
    color_cabello = models.CharField(max_length=10,default='#FFFFFF')#texto
    sexo = models.CharField(max_length=1,choices=SEX,default='H')#texto
    ranking = models.IntegerField(default=0)#entero

    def __unicode__(self):#para llamar
        return self.user #para que tenga nombre

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

class Acertijo(models.Model):
#atributos
    titulo = models.CharField(max_length=500)#texto
    descripcion = models.TextField()#textolargo
    respuesta = models.TextField()#textolargo

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
    icono = models.ImageField(upload_to = '../image/', default = 'pic_folder/None/no-img.jpg')#imagen crear carpeta de default

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
    icono = models.ImageField(upload_to = '../image/', default = 'pic_folder/None/no-img.jpg')#imagen

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name = "Tesoro"
        verbose_name_plural = "Tesoros"
#A
