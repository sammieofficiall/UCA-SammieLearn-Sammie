from django.shortcuts import render

def home(request):
    return HttpResponse('Home Page')

def rooms(request):
    return HttpResponse('ROOM')
