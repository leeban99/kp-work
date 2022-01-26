from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def home(request):
    #return HttpResponse("Hello World")
    return render(request,'a.html')


def profile(request):
    return HttpResponse("On the Profile page")


def expression(request):
    a = request.POST['text1']
    b = request.POST['text2']
    return render(request,'output.html',{'output':"TESTING"})


