"""ts URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tsapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home',views.home),
     path('',views.home),
    path('about',views.about),
    path('Hyderabad',views.Hyderabad),
    path('warangal',views.warangal),
    path('developers',views.developers),
    path('Health_Awareness',views.Health_Awareness),
    path('Menstrual_Hygiene',views.Menstrual_Hygiene),
    path('Education',views.Education),
    path('login',views.login),
    path('Adilabad',views.Adilabad),
    path('karimnagar',views.karimnagar),
    path('RangaReddy',views.RangaReddy),
    path('',views.RangaReddy),
    path('index',views.index),
     path('',views.index),
    path('Nizamabad',views.Nizamabad),
    path('Mahabubnagar',views.Mahabubnagar),
    path('Medak',views.Medak),
    path('Nalgonda',views.Nalgonda),
    path('BirlaMandir',views.BirlaMandir),
    path('kinnarasani',views.kinnarasani),
    path('khammafort',views.khammafort),
    path('badrachalam',views.badrachalam),
    path('charminar',views.charminar),
    path('goloconda',views.goloconda),
    path('ThousandPillarTemple',views.ThousandPillarTemple),
    path('SanghiTemple',views.SanghiTemple),
    path('RajaRajeswara',views.RajaRajeswara),
    path('kuntalawaterfall',views.kuntalawaterfall),
    path('pocherawaterfall',views.pocherawaterfall),
    path('bogatha',views.bogatha),
   
   ]
