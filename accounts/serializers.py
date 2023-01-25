from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from .models import Profile, User, Skill
from django.contrib.auth.models import Group
from django.db import transaction

class CustomRegisterSerializer(RegisterSerializer):
    role = serializers.CharField()
    
    @transaction.atomic
    def custom_signup(self, request, user):
        profile = Profile(user=user)
        profile.save()
        # group = Group.objects.get(name='PROFESSIONAL')
        # if self.data.get('role') == 'handyman':
        #     group = Group.objects.get(name='HANDY_PERSON') 

        # elif self.data.get('role') == 'pro':
        #     group = Group.objects.get(name='PROFESSIONAL')

        # group.user_set.add(user)

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        # fields = '__all__'
        exclude = ('id',)

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'
        # exclude = ('id','user')


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)
    skill = SkillSerializer(read_only=True, many=True)
    class Meta:
        model = User
        fields = [ 'username', 'first_name', 'last_name', 'email', 'profile', 'skill']