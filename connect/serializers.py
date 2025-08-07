# connect/serializers.py

from rest_framework import serializers
from .models import DeveloperProfile, Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'developer', 'title', 'description', 'link']

class DeveloperProfileSerializer(serializers.ModelSerializer):
    projects = ProjectSerializer(many=True, read_only=True)

    class Meta:
        model = DeveloperProfile
        fields = ['id', 'name', 'email', 'bio', 'skills', 'projects']




