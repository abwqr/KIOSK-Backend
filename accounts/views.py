from django.shortcuts import render
from .serializers import ProfileSerializer, UserSerializer, SkillSerializer
from .models import Profile, User, Skill
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
# Create your views here.

from rest_framework import generics


class AllUsersView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer 

class ProfileView(generics.RetrieveUpdateAPIView):
    lookup_url_kwarg = 'user_id'
    lookup_field = 'user_id'
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    
class UserView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer          
          
class SkillView(generics.ListCreateAPIView):
    serializer_class = SkillSerializer 

    def get_queryset(self) :
        user = self.request.user
        return Skill.objects.filter(user=user)

class SkillModifyView(generics.RetrieveUpdateDestroyAPIView):
    # lookup_url_kwarg = 'user_id'
    # lookup_field = 'user_id'
    # queryset = Skill.objects.all()
    serializer_class = SkillSerializer

    def get_queryset(self) :
        user = self.request.user
        return Skill.objects.filter(user=user, pk=self.kwargs['pk'])
