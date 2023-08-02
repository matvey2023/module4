from django.http import HttpResponse
from django.shortcuts import render

def greeting(request):
    return HttpResponse("Домашка по 4 занятию")