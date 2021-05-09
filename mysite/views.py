from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Message

from django.contrib.auth.models import User
from .forms import UserForm, ContactForm
from .models import Contact


# def index(request):
#      return HttpResponse('Hello World')

def profile(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def projects(request):
    template = loader.get_template('projects.html')
    return HttpResponse(template.render())

def listing(request):
    data = {
        "message": Message.objects.all(),
    }

    # here we're passing the data to our template 
    # we can use tags in our template to display our data
    return render(request, "data.html", data)


def index(request):
    users = User.objects.all()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UserForm
    return render(request, 'index.html', context={'users':users, 'form': form})

def contact(request):
    c = Contact.objects.all()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ContactForm

    return render(request, 'contact.html', context={'contacts': c, 'form': form})
