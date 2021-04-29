from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Message

# def index(request):
#      return HttpResponse('Hello World')

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def projects(request):
    template = loader.get_template('projects.html')
    return HttpResponse(template.render())

def listing(request):
    data = {
        "users": Message.objects.all(),
    }

    # here we're passing the data to our template 
    # we can use tags in our template to display our data
    return render(request, "data.html", data)