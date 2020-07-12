from django.db import models
# from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    company_name = models.CharField(max_length=200)
    description = models.TextField(max_length=200)
    owner = models.CharField(max_length=200)
    password = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.IntegerField()


    class Meta:
        verbose_name_plural = 'Profile'

    def __str__(self):
        return self.company_name
    
class Report(models.Model):
    name = models.CharField(max_length=200)
    statement = models.TextField(max_length=200)
    email = models.EmailField()
    phone = models.IntegerField()

    class Meta:
        verbose_name_plural = 'Report'

    def __str__(self):
        return self.name