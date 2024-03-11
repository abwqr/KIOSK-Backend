from django.db import models
from accounts.models import User
from django_countries.fields import CountryField


""""
user_id (FK)
project_name
type (onsite, remote)
description
budget
country
city
status (available, ongoing, completed)
"""

# Create your models here.


"""
date (upload, due)
bids
cities
"""

class Project(models.Model):
    TYPE_CHOICES = (('PROFESSIONAL', 'PROFESSIONAL'), ('HANDYMAN', 'HANDYMAN'))
    STATUS_CHOICES = (('available', 'available'), ('ongoing', 'ongoing'), ('complete', 'complete'))

    employer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='uploaded_project', default="")
    employee = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='working_on')
    project_title = models.CharField(max_length=120)
    project_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    description = models.TextField()
    budget = models.PositiveIntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')
    country = models.CharField(max_length=200, null = True)
    city = models.CharField(max_length=200, null = True)

class Project_Skill(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='skill', default='')
    skill_name = models.CharField(max_length=30, default="", null=True)




