from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=200)
    sector = models.CharField(max_length=200)
    is_active = models.BooleanField(default=False)


class Employee(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=False)
    name = models.CharField(max_length=200, null=False)
    salary = models.IntegerField(null=False)

