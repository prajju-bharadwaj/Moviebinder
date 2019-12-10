from django.shortcuts import render, redirect
from django.http import HttpResponse
from moviebinder.models import Project, Script, Schedule
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def home(request):
    return render(request, "home.html")

def signup(request):
    if request.method == "POST":
        username= request.POST['username']
        email= request.POST['email']
        password=request.POST['password']

        exists= User.objects.filter(username=username).exists()

        if not exists:
            user = User.objects.create_user(username,email,password)
            return redirect('/signin/')

    return render(request,"signup.html")

def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
    
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('/myprojects/') 
        else:
            # Return an 'invalid login' error message.
            return HttpResponse('invalid user') 

    return render(request, "signin.html")

def signout(request):
    logout(request)
    # Redirect to a success page.

def project(request):
    projects = Project.objects.all()
    return render(request, "project.html", {"projects" : projects})

def new_project(request):
    if request.method == 'POST':
        user = request.user
        project_title = request.POST['title']
        company_name = request.POST['company_name']
        description = request.POST['description']
        project_image = request.FILES['project_image']

        project_new = Project.objects.create(user = user, title = project_title, company_name = company_name, description = description, project_image = project_image)
        return redirect('/myprojects/')

    return render(request, "newproject.html")

def project_overview(request,project_id):
    project = Project.objects.get(pk=project_id)
    return render(request, "projectoverview.html", {"project" : project})

def all_scripts(request):
    script = Script.objects.all()
    return render(request, "allscripts.html", {"scripts" : script})

def add_script(request):
    if request.method == 'POST':
        title = request.POST['script_title']
        content = request.POST['script_content']

        new_script = Script.objects.create(script_title = title, script_content = content)
        return redirect('/allscripts/')

    return render(request, "addscript.html")

def script(request,script_id):
    script = Script.objects.get(pk=script_id)
    return render(request, "script.html", {"script" : script})

def edit_script(request,script_id):
    script = Script.objects.get(pk=script_id)
    if request.method == 'POST':
        title = request.POST['script_title']
        content = request.POST['script_content']

        script.script_title = title
        script.script_content = content
        script.save()
        
        return redirect(f'/script/{script_id}/')

    return render(request, "editscript.html", {"script": script}) 