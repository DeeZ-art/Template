from distutils.command.upload import upload
import email
from email.policy import default
from tabnanny import verbose
from unicodedata import name
from unittest.util import _MAX_LENGTH
from django.db import models

#About Model
class About(models.Model):
    short_description= models.TextField()
    description= models.TextField()
    image = models.ImageField(upload_to="about")

    class Meta:
        verbose_name = "About me"
        verbose_name_plural = "About me"
    def __str__(self):
        return "About me"

#Service Model
class Service(models.Model):
    name= models.CharField(max_length=100,verbose_name="Service name")
    description= models.TextField( verbose_name="About services")
    
    def __str__(self):
        return self.name
    
#Recent work Model
class RecentWork(models.Model):
    title= models.CharField(max_length=100,verbose_name="Work title")
    image = models.ImageField(upload_to="works")
    
    def __str__(self):
        return self.title

#Client Model
class ClientModel(models.Model):
    name= models.CharField(max_length=100,verbose_name="Client name")
    description= models.TextField( verbose_name="Client say")
    image = models.ImageField(upload_to="clients",default="default.png")

    def __str__(self):
        return self.name

#Portfolio Model
class Portfolio(models.Model):
    image = models.ImageField(upload_to="portfolio_images")
    heading = models.CharField(max_length=100)
    description = models.TextField()
    filter = models.CharField(max_length=100)
    def __str__(self):
         return self.heading

#Contact Model
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    subject = models.CharField(max_length=50)
    message = models.TextField()
    def __str__(self):
         return self.name