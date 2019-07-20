from __future__ import unicode_literals
from django.db import models
import re


EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
class BlogManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors['first_name'] = 'First name should be at least 2 characters'
        if len(postData['last_name']) < 2:
            errors['last_name'] = 'Last name should be at least 2 characters'
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = 'Please enter a valid email'
        if len(postData['password']) < 8:
            errors['password'] = 'Password should be at least 8 characters'
        if postData['password'] != postData['confirm_password']:
            errors['confirm_password'] = 'Confirm password must match password'
        if User.objects.filter(email = postData['email']): 
            errors['duplicate_email'] = "Sorry! This email is already in use..."
        return errors
    def login_validator(self, postData):
        errors = {}
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = 'Please enter a valid email'
        if len(postData['password']) < 8:
            errors['password'] = 'Password should be at least 8 characters'
        
        return errors


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=70)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BlogManager() 

