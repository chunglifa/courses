from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages

def index(request):
    print('RENDERING INDEX HTML')
    context = {
        'courses': Course.objects.all()
    }
    return render(request, "courses/index.html",context)

def sure(request,id):
    print(id)
    print('ARE YOU SURE YOU WANT TO DELETE??1?!')
    course = Course.objects.get(id=id)
    context = {
        'course': course
    }
    return render(request, "courses/delete.html",context)

def process(request):
    print('START PROCESSING')
    if request.method == 'POST':
        errors = Course.objects.basic_validator(request.POST)
        if len(errors):
            for key, value in errors.items():
                messages.error(request,value)
            return redirect("/")
        else:
            newCourse = Course.objects.create( name = request.POST['name'], desc = request.POST['description'])
        return redirect("/")

def delete(request,id):
    print('DESTROY METHOD - PROCESS')
    print(id)
    Course.objects.get(id = id).delete()
    return redirect("/")
