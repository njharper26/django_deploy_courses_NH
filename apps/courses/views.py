from django.shortcuts import render, redirect
from models import *
from django.contrib import messages

def index(request):
    context = {
        'courses' : Course.objects.all()
    }
    return render(request, 'courses/index.html', context)

def update(request):
    errors = Course.objects.validate(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error)
        return redirect('/')
    else:
        c1 = Course(name=request.POST['html_name'], desc=request.POST['html_desc'])
        c1.save()
        return redirect('/')  

def delete(request, id):
    context = {
        'course' : Course.objects.get(id = id)
    }
    return render(request, 'courses/delete.html', context)

def destroy(request, id):
    c1 = Course.objects.get(id = id)
    c1.delete()
    return redirect('/')


# Create your views here.
