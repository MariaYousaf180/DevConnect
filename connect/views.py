from django.shortcuts import render
from rest_framework import viewsets
from .serializers import DeveloperProfileSerializer
from .models import DeveloperProfile

class DeveloperProfileViewSet(viewsets.ModelViewSet):
    queryset = DeveloperProfile.objects.all()
    serializer_class = DeveloperProfileSerializer
# connect/views.py

from rest_framework import viewsets
from .models import DeveloperProfile, Project
from .serializers import DeveloperProfileSerializer, ProjectSerializer

class DeveloperProfileViewSet(viewsets.ModelViewSet):
    queryset = DeveloperProfile.objects.all()
    serializer_class = DeveloperProfileSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


# Create your views here.
