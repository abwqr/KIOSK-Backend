from django.shortcuts import render
from .serializers import ProfileSerializer, UserSerializer, SkillSerializer, EducationSerializer
from .models import Profile, User, Skill, Education
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication

# Create your views here.

from rest_framework import generics


class AllUsersView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer 

@method_decorator(login_required, name='dispatch')
class ProfileView(generics.RetrieveUpdateAPIView):
    lookup_url_kwarg = 'user_id'
    lookup_field = 'user_id'
    # queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


    def get_queryset(self) :
        user = self.request.user
        return Profile.objects.filter(user=user)
    
class UserView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer          
          
class SkillView(generics.ListCreateAPIView): 
    serializer_class = SkillSerializer 
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # content = {'response':'Please log in'}
        user = self.request.user
        return Skill.objects.filter(user=user)
        

class UpdateSkillView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SkillSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self) :
        user = self.request.user
        return Skill.objects.filter(user=user)

class EducationView(generics.ListCreateAPIView): 
    serializer_class = EducationSerializer 
    # authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Education.objects.filter(user=user)

class UpdateEducationView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EducationSerializer
    permission_classes = [IsAuthenticated]


    def get_queryset(self) :
        user = self.request.user
        return Education.objects.filter(user=user, pk=self.kwargs['pk'])
