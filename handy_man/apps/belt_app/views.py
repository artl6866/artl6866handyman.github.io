from django.shortcuts import render, HttpResponse, redirect
from.models import *
from django.contrib import messages
from datetime import datetime
import bcrypt
from ..app_one.models import *
from ..belt_app.models import *

def main(request):
    current_user = User.objects.get(id=request.session['user_id'])
    all_jobs = Job.objects.all().exclude(user_completing=request.session['user_id'])
    my_jobs = Job.objects.filter(user_completing=current_user)
    context = {
        'user_name' : current_user.fname,
        'my_jobs' : my_jobs,
        'all_jobs' : all_jobs,
    }

    return render(request, 'belt_app/index.html', context)

def add(request):
    current_user = User.objects.get(id=request.session['user_id'])
    context = {
        'user_name' : current_user.fname,
    }
    return render(request, 'belt_app/add.html',context)

def processadd(request):
    if request.method == 'POST':
        errors = Job.objects.job_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request,value)
            return redirect('/belt/processadd')

        current_user = User.objects.get(id=request.session['user_id'])
        job = Job.objects.create(title=request.POST['title'],description=request.POST['description'],location=request.POST['location'],created_by=current_user)
        return redirect('/belt')

    elif request.method == 'GET':
        return render(request,'belt_app/add.html')

def delete(request, id):
    user = User.objects.get(id=request.session['user_id'])
    job = Job.objects.get(id=id)
    job.delete()
    return redirect('/belt')

def show(request, id):
    current_user = User.objects.get(id=request.session['user_id'])
    job = Job.objects.get(id=id)
    context = {
        'this_job' : job,
        'user_name' : current_user.fname,

    }
    return render(request,'belt_app/show.html',context)

def edit(request, id):
    current_user = User.objects.get(id=request.session['user_id'])
    job = Job.objects.get(id=id)
    context ={
        'id':id,
        'title' : Job.objects.get(id=id).title,
        'description' : Job.objects.get(id=id).description,
        'location' : Job.objects.get(id=id).location,
        'user_name' : current_user.fname,
    }
    return render(request,'belt_app/edit.html',context)

def updatejob(request, id):
    if request.method == 'POST':
        errors = Job.objects.job_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
                return redirect('/belt/edit/' + str(id))

        job = Job.objects.get(id=id)
        job.title = request.POST['title']
        job.description = request.POST['description']
        job.location = request.POST['location']
        job.save()

    return redirect('/belt')

def join(request, id):
    if 'user_id' not in request.session:
        return redirect('/belt')
    job = Job.objects.get(id=id)
    current_user = User.objects.get(id=request.session['user_id'])
    job.user_completing = current_user
    job.save()
    return redirect('/belt')

# def remove(request, id):
#     user = User.objects.get(id=request.session['user_id'])
#     job = Job.objects.get(id=id)
#     job.remove()
#     return redirect('/belt')

