from rest_framework import serializers
from .models import Project
class ProjectSerializer(serializers.ModelSerializer):
    
    def create(self, validated_data):
        user =  self.context['request'].user
        # skill_name = validated_data['skill_name']    
    
        obj = Project.objects.create(**validated_data, employer=user)
        obj.save()
        return obj

    
    class Meta:
        model = Project 
        fields = '__all__'