from django.db import models

class DeveloperProfile(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    skills = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Project(models.Model):
    developer = models.ForeignKey(DeveloperProfile, related_name='projects', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    link = models.URLField(blank=True)

    def __str__(self):
        return self.title



    

# Create your models here.
