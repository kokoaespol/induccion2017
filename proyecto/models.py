from django.db import models
from django.contrib.auth.models import User
# Create your models here.
SEX = (
    ('H','Hombre'),
    ('M','Mujer'),
)

#Facultad
class Department(models.Model):
#atributos
    name = models.CharField(max_length=100)#texto

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "Department"
        verbose_name_plural = "Departments"


class Block(models.Model):
#atributos
    name = models.CharField(max_length=100)#texto
#relaciones
    department = models.ForeignKey(Department,default='', related_name='department')#uno a muchos
    
    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "Block"
        verbose_name_plural = "Blocks"


#Llaves para abrir secretos
class TypeR(models.Model):
#atributos
    name = models.CharField(max_length=100)#texto
    description = models.CharField(max_length=100)#texto
    
    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "typeR"
        verbose_name_plural = "typesR"


#Llaves para abrir secretos
class TypeT(models.Model):
    #atributos
    name = models.CharField(max_length=100)#texto
    description = models.CharField(max_length=100)#texto
    
    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "typeT"
        verbose_name_plural = "typesT"


#Llaves para abrir secretos
class KeyR(models.Model):
    #atributos
    name = models.CharField(max_length=100)#texto
    description = models.CharField(max_length=100)#texto
    posX = models.FloatField(null=True, blank=True, default=None)
    posY = models.FloatField(null=True, blank=True, default=None)
    #relaciones
    typeR = models.ForeignKey(TypeR,default='', related_name='typeR')#uno a muchos
    
    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "keyR"
        verbose_name_plural = "keysR"


#Llaves para abrir secretos
class KeyT(models.Model):
    #atributos
    name = models.CharField(max_length=100)#texto
    description = models.CharField(max_length=100)#texto
    posX = models.FloatField(null=True, blank=True, default=None)
    posY = models.FloatField(null=True, blank=True, default=None)
    #relaciones
    typeT = models.ForeignKey(TypeT,default='', related_name='typeT')#uno a muchos
    
    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "keyT"
        verbose_name_plural = "keysT"


#Código de las aulas y oficinas
class Room(models.Model):
    #atributos
    name = models.CharField(max_length=100)#texto
    description = models.CharField(max_length=100)#texto
    #relaciones
    block = models.ForeignKey(Block,default='', related_name='block')#uno a muchos
    keyR = models.ForeignKey(Block,default='', related_name='keyR')#uno a muchos
    
    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "Room"
        verbose_name_plural = "Rooms"



class Medal(models.Model):
#atributos
    name = models.CharField(max_length=50)#texto
    description = models.TextField()#textolargo
    n_puzzle = models.IntegerField()#entero
    #image = models.CharField(max_length=50)#imagen
    image = models.ImageField(upload_to = 'images/', default = 'pic_folder/None/no-img.jpg')#imagen crear carpeta de default

    #profile = models.ManyToManyField(Profile, null=True, blank=True)#muchos a muchos

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "Medal"
        verbose_name_plural = "Medals"


class Mision(models.Model):
#atributos
    name = models.CharField(max_length=500)#texto
    description = models.TextField()#textolargo
#relaciones
    medal = models.ForeignKey(Medal ,default='', related_name='medals')#uno a muchos

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "Mision"
        verbose_name_plural = "Misions"

class Profile(models.Model):
#atributos
    name = models.CharField(max_length=50, null=True, blank=True)#texto
    last_name = models.CharField(max_length=50, null=True, blank=True)#texto
    skin = models.CharField(max_length=10,default='#FFFFFF', null=True, blank=True)#texto
    genre = models.CharField(max_length=3,choices=SEX,default='H', null=True, blank=True)#texto
    ranking = models.IntegerField(default=0, null=True, blank=True)#entero
#relaciones
    user = models.OneToOneField( User, on_delete=models.CASCADE, related_name='user')#uno a uno

    def __unicode__(self):
        return unicode(self.user.username) #para que tenga nombre

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"


class MisionProfile(models.Model):
    #atributos
    name = models.CharField(max_length=50)#texto
    description = models.CharField(max_length=50)#texto
    is_correct = models.BooleanField(default=False)
    #relaciones
    mision = models.ForeignKey(Mision ,default='', related_name='misionprof')#uno a muchos
    profile = models.ForeignKey(Profile ,default='', related_name='profile')#uno a muchos

    def __unicode__(self):
        return self.profile.user.username

    class Meta:
        verbose_name = "MisionProfile"
        verbose_name_plural = "MisionsProfiles"


class Treasure(models.Model):
    name = models.CharField(max_length=50)#texto
    description = models.TextField()#textolargo
    image = models.ImageField(upload_to = 'images/', default = 'pic_folder/None/no-img.jpg')

    room = models.ForeignKey(Room ,default='', related_name='room')#uno a muchos
    keyT = models.ForeignKey(KeyT ,default='', related_name='keyT')#uno a muchos
    mision = models.ForeignKey(Mision ,default='', related_name='mision')#uno a muchos

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "Treasure"
        verbose_name_plural = "Treasures"

