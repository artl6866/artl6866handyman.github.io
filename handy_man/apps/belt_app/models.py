from __future__ import unicode_literals
from django.db import models
import re, bcrypt
from datetime import datetime
from ..app_one.models import *
from . models import *

class JobManager(models.Manager):
    def job_validator(self,postData):
        errors = {}
        if len(postData['title']) < 4:
            errors['titlelength'] = "Please enter title (must be more than 3 characters)."
        if len(postData['description']) < 4:
            errors['descriptionlength'] = "Please enter description (must be more than 3 characters)."
        if len(postData['location']) < 4:
            errors['locationlength'] = "Please enter location (must be be more than 3 characters)."

        return errors


class Job(models.Model):
    title = models.CharField(max_length = 255)
    description = models.TextField()
    location = models.CharField(max_length = 255)
    created_by = models.ForeignKey(User, related_name = 'user_create', on_delete = 'models.CASCADE')
    user_completing = models.ForeignKey(User, related_name='user_title', on_delete='models.CASCADE', null= True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = JobManager()
