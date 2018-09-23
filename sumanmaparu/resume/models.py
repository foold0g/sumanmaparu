from django.db import models

# Create your models here.

class Contact(models.Model):
    email = models.EmailField(default="")
    phone = models.CharField(max_length=18)
    house_number = models.CharField(max_length=3, default="")
    street = models.CharField(max_length=50, default="")
    area = models.CharField(max_length=30, default="")
    city = models.CharField(max_length=30, default="")
    county = models.CharField(max_length=30, default="")
    post_code = models.CharField(max_length=10, default="")
    country = models.CharField(max_length=30, default="")


    def __str__(self):
        return self.email + ' ' + self.phone + ' ' + self.house_number + ' ' + self.street + ' ' + self.area\
               + ' ' + self.city + ' ' + self.county + ' ' + self.post_code + ' ' + self.country


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    company = models.CharField(max_length=30)
    profile_description = models.TextField(blank=True)
    profile_image = models.ImageField(upload_to='profile_pic', blank=True)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    def __str__(self):
        return self.first_name +' '+ self.last_name +' '+ self.company
