from django.db import models  
from django.contrib.auth.models import User


class Person(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)

class Message(models.Model):
    message = models.CharField(max_length=50)
    subject = models.CharField(max_length=30)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

User._meta.get_field('email')._unique = True

class Contact(models.Model):
    email = models.EmailField(max_length=50, unique=False)
    message = models.TextField()