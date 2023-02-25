import datetime
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    now=datetime.datetime.now()
    html="<html><body><h2>now time is %s.</h2></body></html>"%now
    return HttpResponse(html)
def welcome(request):
    return HttpResponse("Welcome to django class")
def  emobilis(request):
    return HttpResponse("Emobilis mobile technology institute")
def home(request):
    return render(request,'home.html')
def service(request):
    return render(request,'services.html')
def about(request):
    return render(request,'about us.html')