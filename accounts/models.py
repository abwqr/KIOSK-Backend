from django.contrib.auth.models import AbstractUser
from django.db import models
# # Create your models here.


class User(AbstractUser):
    pass



class Profile(models.Model):

    GENDER_MALE = 0
    GENDER_FEMALE = 1
    GENDER_CHOICES = [(GENDER_MALE, 'male'), (GENDER_FEMALE, 'female')]
    
    user = models.OneToOneField(User ,on_delete=models.CASCADE, related_name='profile') 
    gender = models.IntegerField(choices=GENDER_CHOICES, null=True)
    description = models.TextField(null=True)

class Skill(models.Model):
    SKILL_CHOICES = [(0, 'Trainee'), (1, 'Novice'), (2, 'Proficient'), (3,'Expert')]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='skill')
    skill_name = models.CharField(max_length=30, null=True, unique=True)
    skill_level = models.IntegerField(choices=SKILL_CHOICES, null=True)

class Education(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='education')
    degree = models.CharField(max_length=30, null=True, unique=True)
    