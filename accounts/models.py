from django.contrib.auth.models import AbstractUser
from django.db import models
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator

# # Create your models here.



class User(AbstractUser):
    pass

def current_year():
    return datetime.date.today().year


def max_value_current_year(value):
    value=value+100
    return MaxValueValidator(current_year())(value)

class Profile(models.Model):

    GENDER_MALE = 0
    GENDER_FEMALE = 1
    GENDER_CHOICES = [(GENDER_MALE, 'male'), (GENDER_FEMALE, 'female')]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile') 
    gender = models.IntegerField(choices=GENDER_CHOICES, null=True)
    description = models.TextField(null=True)

class Skill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='skill', default='')
    skill_name = models.CharField(max_length=30, default="", null=True)
   # skill_description = models.TextField(null=True)

class Education(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='education')
    degree = models.CharField(max_length=100, default="")
    institute = models.CharField(max_length=100, default="")
    graduation_year = models.PositiveIntegerField(default=current_year(), validators=[MinValueValidator(1960), max_value_current_year])

# Create after profile for project id
# class Review(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='education')
#     degree = models.CharField(max_length=100, default="")
#     institute = models.CharField(max_length=100, default="")
#     graduation_year = models.PositiveIntegerField(default=current_year(), validators=[MinValueValidator(1960), max_value_current_year])
