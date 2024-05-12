from django.shortcuts import render
from .models import Personne

# Create your views here.
team = Personne.objects.all()
