from django.db import models
from django.utils import timezone
from django.contrib.gis.db import models
from django.contrib.gis.geos import GEOSGeometry
from django.contrib.auth.models import User

# Create your models here.

class News(models.Model):
  author = models.CharField(max_length=30)
  title = models.CharField(max_length=30)
  description = models.TextField()
  pub_date =  models.DateField(default=timezone.now())

  def __str__(self):
    return self.author


class SportNews(models.Model):
  author = models.CharField(max_length=30)
  title = models.CharField(max_length=30)
  description = models.TextField()
  pub_date =  models.DateField(default=timezone.now())

  def __str__(self):
    return self.author

class RegistrationData(models.Model):
  username =  models.CharField(max_length=100)
  password = models.CharField(max_length=100)
  email = models.CharField(max_length=100)
  phone = models.CharField(max_length=100)

  def __str__(self):
    return self.username


class Publication(models.Model):
  title = models.CharField(max_length=20)

  def __str__(self):
    return self.title

  class Meta: 
    ordering = ("title",)


class Article(models.Model):
  headline = models.CharField(max_length=300)
  publications = models.ManyToManyField(Publication)


  def __str__(self):
    return self.headline

  class Meta: 
    ordering = ("headline",)

class Reporter(models.Model):
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)
  email = models.EmailField()

  def __str__(self):
    return self.first_name

class TheArticle(models.Model):
  headline = models.CharField(max_length=100)
  pub_date = models.CharField(max_length=30)
  reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

  def __str__(self):
    return self.headline
    

  class Meta:
    ordering = ('headline',)


class Place(models.Model):
  name = models.CharField(max_length=30)
  address = models.CharField(max_length=30)

  def __str__(self):
    return self.name

class Restaurant(models.Model):
  name = models.CharField(max_length=30)
  place = models.OneToOneField(Place, on_delete=models.CASCADE, primary_key=True)
  serves_hot_dogs = models.BooleanField(default=False)
  serves_pizza = models.BooleanField(default=False)

  def __str__(self):
    return self.name

  
class NewArticle(models.Model):
  title = models.CharField(max_length=50)
  body = models.TextField()
  date = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.title

  def ShortenText(self):
    return self.body[:100]



class ContactInfo(models.Model):

  name = models.CharField(max_length=40)
  email = models.EmailField(max_length=40)
  address = models.CharField(max_length=30)

  class Meta:
    abstract = True

class Customer(ContactInfo):

  phone = models.CharField(max_length=30)

  def __str__(self):
    return self.name

class Staff(ContactInfo):

  position = models.CharField(max_length=30)

  def __str__(self):
    return self.name

class MyPlace(models.Model):
  name = models.CharField(max_length=40)
  address = models.CharField(max_length=30)

  def __str__(self):
    return self.name

class BurgerBar(Place):
  serves_hot_dogs = models.BooleanField(default=False)
  serves_pizza = models.BooleanField(default=False)

class MyUser(User):

  class Meta:
    ordering = ('username',)

    proxy = True
  
  def fullName(self):
    return self.first_name + " " + self.last_name