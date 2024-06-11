from django.shortcuts import get_object_or_404, render
from contents.models import Personne, Projects, Workshop

# Create your views here.

team = Personne.objects.all()
prjcts = Projects.objects.all()
workshops = Workshop.objects.all()

def index(request):
    prjcts = Projects.objects.all()[:3]
    team = Personne.objects.all()[:4]
    workshops = Workshop.objects.all()[:3]
    return render(request, 'pages/index.html', {'team':team, 'prjcts':prjcts, 'workshops':workshops})


def members(request):
    return render(request, 'pages/team.html', {'team':team})

def projects(request):
    return render(request, 'pages/projects.html', {'prjcts':prjcts, 'team':team})

def project_detail(request, project_id):
    project = get_object_or_404(Projects, pk=project_id)
    return render(request, 'pages/project.html', {'project': project})

def workshop(request):
    return render(request, 'pages/workshop.html', {'workshops':workshops})


def workshop_details(request, workshop_id):
    workshop = get_object_or_404(Workshop, pk=workshop_id)
    organizers = set(workshop.organizer.all())
    speakers = set(Personne.objects.filter(conference__workshop=workshop))
    participants = list(organizers.union(speakers))  # Union of organizers and speakers without repetition
    return render(request, 'pages/workshop_details.html', {
        'workshop': workshop,
        'participants': participants,
    })


def about(request):
    return render(request, 'pages/about.html')