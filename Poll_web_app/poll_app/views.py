from multiprocessing import context
from django.forms import ModelForm
from django.shortcuts import render

from .forms import CreatePollForm
from .models import Poll

# Create your views here.

def Home(request):
    return render(request,"poll_temp/home_temp.html")

def Results(request):
    return render(request,"poll_temp/results_temp.html")

def Create(request):
    form = CreatePollForm()
    context = {'form': form}
    return render(request,"poll_temp/create_temp.html")

def Vote(request):
    return render(request,"poll_temp/vote.html")