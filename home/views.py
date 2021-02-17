import datetime

from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
from home.models import register

def home(request):
    return (render ,'admin')