from django.shortcuts import render
from django.http import HttpResponse
from . import taskForm

# Create your views here.

def index(request):
    return HttpResponse("Welcome to task manager")

def welcome(request):

    if "tasks" not in request.session:
        request.session["tasks"] = []
    return render(request, "tasks/welcomeToTask.html", {"tasks":request.session["tasks"]})

def add(request):
   
    if "tasks" not in request.session:
        print(f"new session")
        request.session["tasks"] = []

    if request.method == 'POST':

        form = taskForm.TaskForm(request.POST)

        if form.is_valid() :
            print(form.cleaned_data)
            task = form.cleaned_data["task"]

            print(task)

            request.session["tasks"] += [task]
            form = taskForm.TaskForm()  
    else:
        form = taskForm.TaskForm()  
    print(request.session["tasks"])
    print(f"task length : {len(request.session['tasks'])}")
    return render(request, "tasks/add.html",{"form":form, "tasks":request.session["tasks"]})


def clear(request):

    if "tasks" in request.session :
        request.session["tasks"] = []
    
    return render(request, "tasks/add.html")
