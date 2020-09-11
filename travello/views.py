from django.shortcuts import render
from .models import Destination
from django.http import HttpResponse
def home(request):


    dests = Destination.objects.all()

    return render(request,'index.html', {'dests':dests})