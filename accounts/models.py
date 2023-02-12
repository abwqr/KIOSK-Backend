from django.contrib.auth.models import AbstractUser
from django.db import models
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
from django_countries.fields import CountryField
import datetime

# # Create your models here.


YEAR_CHOICES = []
for r in range(1980, (datetime.datetime.now().year)):
    YEAR_CHOICES.append((r,r))
    
class User(AbstractUser):
    pass

def current_year():
    return datetime.date.today().year


def max_value_current_year(value):
    value=value+5
    return MaxValueValidator(current_year())(value)

class Profile(models.Model):

    GENDER_CHOICES = (("male", "male"), ("female", "female"), ("other", "other"))

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile') 
    gender =  models.CharField(
        max_length=20,
        choices = GENDER_CHOICES,
        null= True
        )
    description = models.TextField(null=True)
    age = models.PositiveIntegerField(null = True)
    # country = CountryField()
    country = models.CharField(max_length=200, null = True)
    city = models.CharField(max_length=200, null = True)



class Skill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='skill', default='')
    skill_name = models.CharField(max_length=30, default="", null=True)
   # skill_description = models.TextField(null=True)

class Education(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='education')
    degree = models.CharField(max_length=100, default="")
    institute = models.CharField(max_length=100, default="")
    # graduation_year = models.PositiveIntegerField(default=current_year(), validators=[MinValueValidator(1960), max_value_current_year])
    graduation_year = models.CharField(max_length=4)

class Experience(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='experience')
    title = models.CharField(max_length=50)
    company = models.CharField(max_length=100, null=True)
    start_year = models.CharField(max_length=4)
    end_year = models.CharField(max_length=10)
    description = models.TextField(null = True)

   

# Create after profile for project id
# class Review(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='education')
#     degree = models.CharField(max_length=100, default="")
#     institute = models.CharField(max_length=100, default="")
#     graduation_year = models.PositiveIntegerField(default=current_year(), validators=[MinValueValidator(1960), max_value_current_year])
