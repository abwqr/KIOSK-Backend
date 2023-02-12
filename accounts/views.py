from django.shortcuts import render
from .serializers import ProfileSerializer, UserSerializer, SkillSerializer, EducationSerializer, ExperienceSerializer
from .models import Profile, User, Skill, Education, Experience
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication

from rest_framework.decorators import api_view

# Create your views here.

from rest_framework import generics
from django.views.generic import ListView

class AllUsersView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer 

# class UserView(generics.RetrieveUpdateAPIView):
#     serializer_class = UserSerializer
#     def get_queryset(self):
#         user = self.request.user
#         print(user.id)
#         return User.objects.filter(id=user.id)

class UserView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    def get(self, request):
        user = request.user
        print(user)
        user = User.objects.filter(id=user.id)
        # print(profile)
        s = UserSerializer(user, many=True)
        return Response(s.data)
    

          
class ProfileView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProfileSerializer
    def get(self, request, user_id):
        user = user_id
        print(user)
        # if user.groups.filter(name='PROFESSIONAL').exists():
        #     print("P")
        # print(user)
        profile = Profile.objects.filter(user_id=user)
        print(profile)
        s = ProfileSerializer(profile, many=True)
        return Response(s.data)
    
class UpdateProfileView(APIView):

    permission_classes = [IsAuthenticated]
    serializer_class = ProfileSerializer
    
    def get(self, request):
        user = request.user
        print(user)
        # if user.groups.filter(name='PROFESSIONAL').exists():
        #     print("P")
        # print(user)
        profile = Profile.objects.filter(user=user)
        print(profile) 
        s = ProfileSerializer(profile, many=True)
        return Response(s.data)


    permission_classes = [IsAuthenticated]
    serializer_class = ProfileSerializer
    def post(self, request):
        user = request.user
        profile = get_object_or_404(Profile.objects.all(), user=user)
        serializer = ProfileSerializer(profile, data=request.data, partial=True)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class CreateSkillView(generics.ListCreateAPIView): 
    serializer_class = SkillSerializer 
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        print(user)
        return Skill.objects.filter(user=user)

class SkillView(generics.ListAPIView): 
    serializer_class = SkillSerializer 
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        
        return Skill.objects.filter(user=user_id)

        
class UpdateSkillView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SkillSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self) :
        user = self.request.user
        return Skill.objects.filter(user=user)





class CreateEducationView(generics.ListCreateAPIView): 
    serializer_class = EducationSerializer 
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        print(user)
        return Education.objects.filter(user=user)

class EducationView(generics.ListAPIView): 
    serializer_class = EducationSerializer 
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        
        return Education.objects.filter(user=user_id)

        
class UpdateEducationView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EducationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self) :
        user = self.request.user
        return Education.objects.filter(user=user)



class CreateExperienceView(generics.ListCreateAPIView): 
    serializer_class = ExperienceSerializer 
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        print(user)
        return Experience.objects.filter(user=user)

class ExperienceView(generics.ListAPIView): 
    serializer_class = ExperienceSerializer 
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        
        return Experience.objects.filter(user=user_id)

        
class UpdateExperienceView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ExperienceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self) :
        user = self.request.user
        return Experience.objects.filter(user=user)






# class EducationView(generics.ListCreateAPIView): 
#     serializer_class = EducationSerializer 
#     permission_classes = [IsAuthenticated]

#     def get_queryset(self):
#         user = self.request.user
#         return Education.objects.filter(user=user)

# class UpdateEducationView(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = EducationSerializer
#     permission_classes = [IsAuthenticated]


#     def get_queryset(self) :
#         user = self.request.user
#         return Education.objects.filter(user=user, pk=self.kwargs['pk'])

# class ExperienceView(generics.ListCreateAPIView): 
#     serializer_class = ExperienceSerializer 
#     permission_classes = [IsAuthenticated]

#     def get_queryset(self):
#         user = self.request.user
#         return Experience.objects.filter(user=user)

# class UpdateExperienceView(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = ExperienceSerializer
#     permission_classes = [IsAuthenticated]


#     def get_queryset(self) :
#         user = self.request.user
#         return Experience.objects.filter(user=user, pk=self.kwargs['pk'])
