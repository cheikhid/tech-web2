from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name = 'home'),
    path('projects/', views.projects, name = 'projects'),
    path('project/<int:project_id>/', views.project_detail, name = 'project'),
    path('team/', views.members, name = 'team'),
    path('about/', views.about, name = 'about'),
    path('workshops/', views.workshop, name = 'workshop'),
    path('workshop/<int:workshop_id>/', views.workshop_details, name = 'workshop'),
]