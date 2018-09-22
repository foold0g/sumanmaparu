from django.db import models
from django.core.files.storage import FileSystemStorage

# Create your models here.

class Person(models.Model):
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)
  company = models.CharField(max_length=30)
  profile_image = models.ImageField(upload_to='profile_pic', blank=True)

  def __str__(self):
    return self.first_name +' '+ self.last_name +' '+ self.company
