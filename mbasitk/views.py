from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render (request,'index.html',{'key1':' I am coming from new making website'})

def result (request):
    age = request.GET['user_name']
    name = request.GET['user_age']
    message = f' HI {name}, you are {age} years old .'
    return render(request,'result.html',{'message' :message, 'age':age })

