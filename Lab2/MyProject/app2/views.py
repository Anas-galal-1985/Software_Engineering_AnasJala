from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def Print_app2(request):
    return HttpResponse("Hello App2")