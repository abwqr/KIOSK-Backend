from django.shortcuts import render
from .serializers import ProjectSerializer
from .models import Project
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication
from rest_framework import generics

""""
checks:
employer != employee
""" 
class ProjectView(generics.ListCreateAPIView):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        project = Project.objects.filter(employer=user)
        return project

class SingleProjectView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProjectSerializer
    
    def get_queryset(self):
        user = self.request.user
        project = Project.objects.filter(user=user, pk=self.kwargs['pk'])
        return project