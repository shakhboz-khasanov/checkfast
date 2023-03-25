from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

from django.conf import settings
from django.urls import reverse
import json
import os
# Create your models here.

class Account(AbstractUser):
  
  #Multiple choice field
  OPTIONS = [
  ('Teacher', 'Teacher'),
  ('Student', 'Student'),
  ('Researcher', 'Researchers'),
  ('Others', 'Others'),
  ]
  selection = models.CharField(choices=OPTIONS, null=True, blank=True, max_length=100)
  
  #Multiple choice field
  REGIONS = [
  ('Andijan', 'Andijan'),('Namangan', 'Namangan'),('Surkhandarya', 'Surkhandarya'),
  ('Bukhara', 'Bukhara'),('Samarkand', 'Samarkand'),('Tashkent', 'Tashkent'),
  ('Jizzakh', 'Jizzakh'),('Sirdarya', 'Sirdarya'),('Fergana', 'Fergana'),
  ('Kashkadarya', 'Kashkadarya'),('Navoi', 'Navoi'),('Khorezm', 'Khorezm'),('Karakalpakstan','Karakalpakstan')
  ]
  region = models.CharField(choices=REGIONS, null=True, blank=True, max_length=100)
  #Related Variables
  #user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
  slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
  coins = models.IntegerField(default=50)
  
  def __str__(self):
    return '{}{}'.format(self.username)

  def get_absolute_url(self):
    return reverse('account-detail', kwargs={'username': self.username})

  def save(self, *args, **kwargs):
    self.slug = slugify('{}{}'.format(self.username,self.first_name))
    super(Account, self).save(*args, **kwargs)

