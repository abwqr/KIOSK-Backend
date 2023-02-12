from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from .models import Profile, User, Skill, Education, Experience
from django.contrib.auth.models import Group
from django.db import transaction
from rest_framework.validators import UniqueTogetherValidator
from rest_framework.authtoken.models import Token

class CustomRegisterSerializer(RegisterSerializer):
    role = serializers.CharField()
    
    @transaction.atomic
    def custom_signup(self, request, user):
        profile = Profile(user=user)
        profile.save()

        # group = Group.objects.get(name='PROFESSIONAL')
        if self.data.get('role') == 'handyman':
            group = Group.objects.get(name='HANDYMAN') 
            group.user_set.add(user)
        # elif self.data.get('role') == 'professional':
            print(group)

        else:
            group = Group.objects.get(name='PROFESSIONAL')
            group.user_set.add(user)

        
        print(group)


class ProfileSerializer(serializers.ModelSerializer):
    
    # def create(self, validated_data):
    #     user =  self.context['request'].user
    #     # if Profile.objects.filter(user=user).exists():
    #     #     raise serializers.ValidationError("Profile already exists!")

    #     # else:
    #     obj = Profile.objects.update_or_create(**validated_data, user=user)
    #     obj.save()
    #     return obj

    # def update(self, instance, validated_data):
    #     instance.gender = validated_data.get('gender', instance.gender)
    #     instance.age = validated_data.get('age', instance.age)
    #     instance.city = validated_data.get('city', instance.city)
    #     instance.country = validated_data.get('country', instance.country)
    #     instance.description = validated_data.get('description', instance.description)

    #     instance.save()
    #     return instance
    class Meta:
        model = Profile
        # fields = '__all__'
        fields = ['gender','city', 'country','description','age']
        depth = 1
        # exclude = ('id',)

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
        # degree = validated_data['degree']    
        # if Education.objects.filter(user=user, degree = degree).exists():
        #     raise serializers.ValidationError("Degree already exists!")

        # else:
        obj = Education.objects.create(**validated_data, user=user)
        obj.save()
        return obj
    
    
class ExperienceSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user =  self.context['request'].user

        obj = Experience.objects.create(**validated_data, user=user)
        obj.save()
        return obj
    class Meta:
        model = Experience
        # fields = '__all__'
        exclude = ('user',)
    
class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True, many=False)
    skill = SkillSerializer(read_only=True, many=True)
    education = EducationSerializer(read_only=True, many=True)
    experience = ExperienceSerializer(read_only=True, many=True)

    class Meta:
        model = User
        # fields = [ 'id', 'username', 'first_name', 'last_name', 'email']
        fields = [ 'id', 'username', 'first_name', 'last_name', 'email', 'profile', 'skill', 'education', 'experience']
    
    