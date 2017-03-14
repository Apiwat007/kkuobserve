from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

import requests
# Create your views here.
def index(request):
	r = requests.get('https://github.com/timeline.json')
	print r.text
	return HttpResponse('<pre>' + r.text + '<pre>')
    # return HttpResponse('Hello from Python!')
    #return render(request, 'index.html')


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

