from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from .models import Profile, User, Skill, Education
from django.contrib.auth.models import Group
from django.db import transaction
from rest_framework.validators import UniqueTogetherValidator

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
        exclude = ('id','user')

class SkillSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user =  self.context['request'].user
        skill_name = validated_data['skill_name']    
        if Skill.objects.filter(user=user, skill_name = skill_name).exists():
            raise serializers.ValidationError("Skill already exists!")

        else:
            obj = Skill.objects.create(**validated_data, user=user)
            obj.save()
            return obj
    

    
    class Meta:
        model = Skill
        # fields = '__all__'
        exclude = ('user',)


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        # fields = '__all__'
        exclude = ('user',)
    
    def create(self, validated_data):
        user =  self.context['request'].user
        degree = validated_data['degree']    
        if Education.objects.filter(user=user, degree = degree).exists():
            raise serializers.ValidationError("Degree already exists!")

        else:
            obj = Education.objects.create(**validated_data, user=user)
            obj.save()
            return obj
    


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True, many=False)
    skill = SkillSerializer(read_only=True, many=True)
    education = EducationSerializer(read_only=True, many=True)
    class Meta:
        model = User
        fields = [ 'username', 'first_name', 'last_name', 'email', 'profile', 'skill', 'education']