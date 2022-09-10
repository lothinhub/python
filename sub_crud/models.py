from email.mime import image
from unicodedata import name
from django.db import models
import datetime
import os
# Create your models here.
def filepath(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('uploads/', filename)

class Employees(models.Model):
    image = models.ImageField(upload_to ='media/',null=True)
    name = models.CharField(max_length=255, blank=True)    
    email = models.EmailField(max_length=255, blank=True)
    address = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=255, blank=True)
    
    # class Meta:
    #     db_table = "student"
    
    # def __str__(self):
    #     return self.name