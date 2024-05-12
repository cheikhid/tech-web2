from django.shortcuts import render
from contents.views import team

# Create your views here.
def index(request):
    return render(request, 'pages/index.html', {'team':team})


def members(request):
    return render(request, 'pages/team.html', {'team':team})