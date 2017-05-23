from django.db import models
from django.contrib.auth.models import User
# Create your models here.
SEX = (
    ('H','Hombre'),
    ('M','Mujer'),
)

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

class Medal(models.Model):
#atributos
    name = models.CharField(max_length=50)#texto
    description = models.TextField()#textolargo
    n_puzzle = models.IntegerField()#entero
    #image = models.CharField(max_length=50)#imagen
    image = models.ImageField(upload_to = 'images/', default = 'pic_folder/None/no-img.jpg')#imagen crear carpeta de default
#relaciones
    block = models.ForeignKey(Block,default='', related_name='blocks')#uno a muchos
    #profile = models.ManyToManyField(Profile, null=True, blank=True)#muchos a muchos

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "Medal"
        verbose_name_plural = "Medals"


class Puzzle(models.Model):
#atributos
    name = models.CharField(max_length=500)#texto
    description = models.TextField()#textolargo
#relaciones
    medal = models.ForeignKey(Medal ,default='', related_name='medals')#uno a muchos

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "Puzzle"
        verbose_name_plural = "Puzzles"

class Profile(models.Model):
#atributos
    name = models.CharField(max_length=50, null=True, blank=True)#texto
    last_name = models.CharField(max_length=50, null=True, blank=True)#texto
    skin = models.CharField(max_length=10,default='#FFFFFF', null=True, blank=True)#texto
    shirt = models.CharField(max_length=10,default='#FFFFFF', null=True, blank=True)#texto
    hair = models.CharField(max_length=10,default='#FFFFFF', null=True, blank=True)#texto
    genre = models.CharField(max_length=3,choices=SEX,default='H', null=True, blank=True)#texto
    ranking = models.IntegerField(default=0, null=True, blank=True)#entero
#relaciones
    user = models.OneToOneField( User, on_delete=models.CASCADE, related_name='user')#uno a uno

    def __unicode__(self):
        return unicode(self.user.username) #para que tenga nombre

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"


class PuzzleProfile(models.Model):
#atributos
    is_correct = models.BooleanField(default=False)
#relaciones
    puzzle = models.ForeignKey(Puzzle ,default='', related_name='puzzlesprof')#uno a muchos
    profile = models.ForeignKey(Profile ,default='', related_name='profiles')#uno a muchos

    def __unicode__(self):
        return self.profile.user.username

    class Meta:
        verbose_name = "PuzzleProfile"
        verbose_name_plural = "PuzzlesProfiles"


class Treasure(models.Model):
    name = models.CharField(max_length=50)#texto
    description = models.TextField()#textolargo
    image = models.ImageField(upload_to = 'images/', default = 'pic_folder/None/no-img.jpg')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "Treasure"
        verbose_name_plural = "Treasures"


class PuzzleTreasure(models.Model):
#relaciones
    puzzle = models.ForeignKey(Puzzle ,default='', related_name='puzzlestreas')#uno a muchos
    treasure = models.ForeignKey(Treasure ,default='', related_name='treasures')#uno a muchos

    def __unicode__(self):
        return self.treasure.name

    class Meta:
        verbose_name = "PuzzleTreasure"
        verbose_name_plural = "PuzzleTreasures"

class Option(models.Model):
#relaciones
    puzzle = models.ForeignKey(Puzzle,on_delete=models.CASCADE, related_name='options')
#atributos
    name = models.TextField()
    is_answer = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "Option"
        verbose_name_plural = "Options"
#A
