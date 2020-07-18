from django.db import models

# Create your models here.
class Company(models.Model):
    companyName = models.CharField(primary_key=True, max_length=200)
    isIndian = models.BooleanField(max_length=200)
    companySummary = models.TextField()