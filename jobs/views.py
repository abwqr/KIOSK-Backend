from django.shortcuts import render
from .serializers import ProjectSerializer, ProjectSkill_Serializer
from .models import Project, Project_Skill, User
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

class TestProjectSkillView(generics.ListAPIView):
    serializer_class = ProjectSkill_Serializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        skill = Project_Skill.objects.all()
        return skill


class ProjectSkillView(generics.ListCreateAPIView):
    serializer_class = ProjectSkill_Serializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'project_id'
    lookup_url_kwarg = 'project_id'

    def get_queryset(self):
        user = self.request.user
        project_id = self.kwargs['project_id']
        project = Project.objects.filter(employer=user, pk=project_id).first()
        
        if project == None:
            return project 
        else:
            skill = Project_Skill.objects.filter(project=project)
            return skill

class ListProjectSkillView(generics.ListAPIView):
    serializer_class = ProjectSkill_Serializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.kwargs['project_id']
        project_id = self.kwargs['project_id']
        project = Project.objects.filter(employer=user, pk=project_id).first()
        print(user)
        if project == None:
            return project 
        else:
            skill = Project_Skill.objects.filter(project=project)
            return skill


class Update_Project_Skill_View(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProjectSkill_Serializer
    
    def get_queryset(self):
        user = self.request.user
        project_id = self.kwargs['project_id']
        project = Project.objects.filter(employer=user, pk=project_id).first()
        print(project)
        if project == None:
            return project
        else:
            skill = Project_Skill.objects.filter(project=project,  pk=self.kwargs['pk'])
            return skill
       
        # user = self.request.user
        # project = Project.objects.filter(employer=user, pk=self.kwargs['pk'])
        # return project
class TestProjectView(generics.ListAPIView):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        project = Project.objects.all()
        return project


class AllProjectView(generics.ListAPIView):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        type = 'HANDYMAN'
        user = self.request.user
        if user.groups.filter(name='PROFESSIONAL').exists():
            type = 'PROFESSIONAL'

        project = Project.objects.filter(project_type=type)
        return project

class ProjectView(generics.ListCreateAPIView):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        project = Project.objects.filter(employer=user)
        return project

class ListProjectView(generics.ListAPIView):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        print(user_id)
        # user = User.objects.get(id=user_id)
        # print(user)
        # user = self.request.user
        project = Project.objects.filter(employer=user_id)
        return project


class UpdateProjectView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProjectSerializer
    
    def get_queryset(self):
        user = self.request.user
        project = Project.objects.filter(employer=user, pk=self.kwargs['pk'])
        return project