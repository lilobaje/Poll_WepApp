from django.shortcuts import render

# Create your views here.

def Home(request):
    return render("home_temp.html")

def Results(request):
    return render("results_temp.html")

def Create(request):
    return render("create_temp.html")