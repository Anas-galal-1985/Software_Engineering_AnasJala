from django.shortcuts import render

# Create your views here.
def index(request):
    name={"fname":"Anas"}
    return render(request, 'index.html',name)
def home(request):
    return render(request, 'home.html')

def showw(request):
    return render(request, 'show.html')

def editt(request):
    s={"total":300,
       "marks":{
           "web":100,
           "netw.":100,
           "algorithm":90,
       }
    }
    return render(request, 'edit.html',s)

def dell(request):
    return render(request, 'delete.html')