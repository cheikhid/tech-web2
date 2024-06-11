from django.shortcuts import render
from .models import Personne, Projects

# Create your views here.
team = Personne.objects.all()

projects = Projects.objects.all()

