from rest_framework import serializers
from .models import Project, Project_Skill

class ProjectSkill_Serializer(serializers.ModelSerializer):

    def create(self, validated_data):
        project_id = self.context.get('request').parser_context.get('kwargs').get('project_id')
        project =  Project.objects.get(id = project_id)   
        obj = Project_Skill.objects.create(**validated_data, project=project)
        obj.save()
        return obj
    
    class Meta:
        model = Project_Skill
        fields = '__all__'
        # exclude = ('project',)
        # depth=1



class ProjectSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user =  self.context['request'].user
        # skill_name = validated_data['skill_name']    
        type = 'None'
        if user.groups.filter(name='PROFESSIONAL').exists():
            type = 'PROFESSIONAL'

        elif user.groups.filter(name='HANDYMAN').exists():
            type = 'HANDYMAN'

        obj = Project.objects.create(**validated_data, employer=user, project_type=type)
        obj.save()
        return obj

    skill = ProjectSkill_Serializer(read_only=True, many=True)

    class Meta:
        model = Project 
        fields = [ 'id','project_title','description','budget','country','city','employee', 'skill']
        # fields = [ 'id','project_title','project_type','description','budget','status','country','city','employer','employee', 'skill']
        # fields = '__all__'
        # exclude = ('employer','project_type','status')
        # depth = 1