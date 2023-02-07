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

    TYPE_HANDYMAN = 0
    TYPE_PRO = 1
    TYPE_CHOICES = [(TYPE_PRO, 'professional'), (TYPE_HANDYMAN, 'handyman')]

    STATUS_AVAILABLE = 0
    STATUS_ONGOING = 1
    STATUS_COMPLETE = 2
    STATUS_CHOICES = [(STATUS_AVAILABLE, 'available'), (STATUS_ONGOING, 'ongoing'), (STATUS_COMPLETE, 'complete')]



    employer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='uploaded_project', default="")
    employee = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='working_on')
    project_title = models.CharField(max_length=120)
    project_type = models.IntegerField(choices=TYPE_CHOICES)
    description = models.TextField()
    budget = models.PositiveIntegerField()
    status = models.IntegerField(choices=STATUS_CHOICES)
    country = CountryField()


