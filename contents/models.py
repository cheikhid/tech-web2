from django.db import models

# Create your models here.
class Personne (models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    photo = models.FileField(upload_to='Team photos')
    post = models.CharField(max_length=100)
    university = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name



class Projects (models.Model):
    title = models.CharField(max_length=100)
    photo = models.FileField(upload_to='projects photos')
    def __str__(self):
        return self.title



class Topics (models.Model):
    title = models.CharField(max_length=100)
    publishedDate = models.DateField()
    github = models.EmailField()
    paper = models.FileField(upload_to='topics file pdf')
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)    
    def __str__(self):
        return self.title


class Workshop (models.Model):
    title = models.CharField(max_length=100)
    photo = models.FileField(upload_to='workshops photos')
    venue = models.CharField(max_length=100) 
    date = models.DateField()
    description = models.TextField()
    organizer = models.ForeignKey(Personne, on_delete=models.CASCADE) 
    def __str__(self):
        return self.title


class Conference(models.Model):
    title = models.CharField(max_length=100)
    speaker = models.ForeignKey(Personne, on_delete=models.CASCADE) 
    time = models.CharField(max_length=100)
    Workshop = models.ForeignKey(Workshop, on_delete=models.CASCADE) 
    def __str__(self):
        return self.title


