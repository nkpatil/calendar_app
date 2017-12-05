from __future__ import unicode_literals
from django.db import models

class Record(models.Model):
    """A database model to store the school teacher records"""
    user = models.CharField(max_length=100, help_text="School Name")
    teacher_name = models.CharField(max_length=100, help_text="Teacher Name")
    grade = models.IntegerField(help_text="Teacher grade number")
    timestamp = models.DateTimeField(help_text="Date time")
    district = models.CharField(max_length=100, help_text="District Name")
    comments = models.CharField(max_length=1000, help_text="Comments (optional)")
