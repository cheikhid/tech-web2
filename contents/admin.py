from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Personne)
admin.site.register(models.Projects)
admin.site.register(models.Topics)
admin.site.register(models.Workshop)
admin.site.register(models.Conference)