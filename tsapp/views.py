from django.shortcuts import render

# Create your views here.
def home(request):
    d={
        'title':'home',
    }
    return render(request,'home.html',d)

def about(request):
    d={
        'title':'about',
    }
    return render(request,'about.html',d)

def Hyderabad(request):
    return render(request,'Hyderabad.html')
def warangal(request):
    return render(request,'warangal.html')
def developers(request):
    return render(request,'developers.html')
def Adilabad(request):
    return render(request,'Adilabad.html')
def karimnagar(request):
    return render(request,'karimnagar.html')
def RangaReddy(request):
    return render(request,'RangaReddy.html')
def index(request):
    return render(request,'index.html')
def Nizamabad(request):
    return render(request,'Nizamabad.html')
def Mahabubnagar(request):
    return render(request,'Mahabubnagar.html')
def Medak(request):
    return render(request,'Medak.html')
def Nalgonda(request):
    return render(request,'Nalgonda.html')
def kinnarasani(request):
   return render(request,'kinnarasani.html')
def khammafort(request):
   return render(request,'khammafort.html')
def badrachalam(request):
   return render(request,'badrachalam.html')
def charminar(request):
    return render(request,'charminar.html')
def goloconda(request):
    return render(request,'goloconda.html')
def thousandpillars(request):
    return render(request,'thousandpillars.html')
def BirlaMandir(request):
    return render(request,'BirlaMandir.html')
def ThousandPillarTemple(request):
    return render(request,'ThousandPillarTemple.html')
def SanghiTemple(request):
    return render(request,'SanghiTemple.html')
def RajaRajeswara(request):
    return render(request,'RajaRajeswara.html')
def kuntalawaterfall(request):
    return render(request,'kuntalawaterfall.html')
def pocherawaterfall(request):
    return render(request,'pocherawaterfall.html')
def bogatha(request):
    return render(request,'bogatha.html')






def Health_Awareness(request):
    d = {
        'title':"health_awareness",
    }
    return render(request,"health_awareness.html",d)

def Menstrual_Hygiene(request):
    return render(request,"menstrual_hygiene.html")

def Education(request):
    return render(request,"education.html")

def login(request):
    return render(request,'login.html')
    