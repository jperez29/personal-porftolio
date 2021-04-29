from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)

class Message(models.Model):
    message = models.CharField(max_length=50)
    subject = models.CharField(max_length=30)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
