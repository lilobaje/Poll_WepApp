from django.shortcuts import render

# Create your views here.
def admin_home(request):
    return render(request,"poll_temp/base_template.html")


def Home(request):
    return render(request,"poll_temp/home_temp.html")

def Results(request):
    return render(request,"poll_temp/results_temp.html")

def Create(request):
    return render(request,"poll_temp/create_temp.html")