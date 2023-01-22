from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.db import transaction

class CustomRegisterSerializer(RegisterSerializer):
    role = serializers.CharField()
    
    @transaction.atomic
    def save(self, request):
        user = super().save(request)
        user.save()

        group = Group.objects.get(name='PROFESSIONAL')
        if self.data.get('role') == 'handyman':
            group = Group.objects.get(name='HANDY_PERSON') 

        elif self.data.get('role') == 'pro':
            group = Group.objects.get(name='PROFESSIONAL')
    
        group.user_set.add(user)


        return user
    # def create(self, validated_data):
    #     user = User.objects.create(
    #     username=validated_data['username'],
    #     email=validated_data['email'],
    #     password1=validated_data['password1'],
    #     password2=validated_data['password2']
    #     )
    #     user.set_password(validated_data['password'])
    #     user.save()

        