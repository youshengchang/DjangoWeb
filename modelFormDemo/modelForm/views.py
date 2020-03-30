from django.shortcuts import render
from modelForm.forms import ProjectForm
from modelForm.models import Project

# Create your views here.
def index(request):
    return render(request, 'modelForm/index.html')

def listProjects(request):
    projectList = Project.objects.all()
    return render(request,'modelForm/listProjects.html',{'projects':projectList})

def addProject(request):
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    return render(request,'modelForm/addProject.html',{'form':form})
