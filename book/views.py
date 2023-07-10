from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import ProjectForm
from .models import Project
# Create your views here.


def projects(request):
    project = Project.objects.all()
    contex = {'projects':project}
    return render(request,'projects.html',contex)

def project(request,pk):
    projectObj = Project.objects.get(id=pk)
    return render(request,'single-project.html',{'project':projectObj})

def create(request):
    form = ProjectForm()
    if request.method == "POST":
        print(request.POST)
        form = ProjectForm(request.POST)
        form.is_valid()
        form.save()
        return redirect('projects')
    context = {'form':form}
    return render(request,'create-form.html',context)