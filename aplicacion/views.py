from django.shortcuts import render
from django.http import HttpResponse	

from django.template import loader

def index(request):
	return HttpResponse("aloha")

def detail(request, aerosol_id):
	return HttpResponse("color: %s" % aerosol_id)

def results(request, aerosol_id):
	response= "you're lookin at the result of question %s"
	return HttpResponse(response % aerosol_id)

def index(request):
    
	return render(request, 'aplicacion/index.html')





# Create your views here.
