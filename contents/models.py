from django.db import models

# Create your models here.
class Personne (models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=200, null=True, blank= True)
    photo = models.FileField(upload_to='Team photos', null=True, blank= True)
    post = models.CharField(max_length=100, null=True, blank= True)
    university = models.CharField(max_length=100, null=True, blank= True)
    facebook = models.CharField(max_length=100 , null=True, blank= True)
    linkedin = models.CharField(max_length=100 , null=True, blank= True)

    
    def __str__(self):
        return self.name



class Projects (models.Model):
    title = models.CharField(max_length=100)
    photo = models.FileField(upload_to='projects photos' )
    def __str__(self):
        return self.title



class Topics (models.Model):
    title = models.CharField(max_length=100)
    publishedDate = models.DateField(null=True, blank= True)
    github = models.CharField(max_length=100 , null=True, blank= True)
    paper = models.FileField(upload_to='topics file pdf', null=True, blank= True)
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)    
    def __str__(self):
        return self.title


class Workshop (models.Model):
    title = models.CharField(max_length=100)
    photo = models.FileField(upload_to='workshops photos', null=True, blank= True)
    venue = models.CharField(max_length=100, null=True, blank= True) 
    date = models.DateField(null=True, blank= True)
    description = models.TextField(null=True, blank= True)
    organizer = models.ManyToManyField(Personne) 
    def __str__(self):
        return self.title


class Conference(models.Model):
    title = models.CharField(max_length=100)
    speaker = models.ForeignKey(Personne, on_delete=models.CASCADE, null=True, blank= True) 
    time = models.CharField(max_length=100, null=True, blank= True)
    workshop = models.ForeignKey(Workshop, on_delete=models.CASCADE) 
    def __str__(self):
        return self.title


