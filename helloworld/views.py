from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.

def index(request):
    time = datetime.datetime.now()
    return HttpResponse('The current date and time are %s.' % time)