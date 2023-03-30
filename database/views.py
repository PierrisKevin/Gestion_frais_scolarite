from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

def loginViews(request):
    if request.method=="POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect("dashboard")
    return render(request, './login.html')

def disconnect(request):
    print("En deconnextion de l'utlisateur", request.user)
    logout(request)
    return redirect("login")
