from django.db import models

# Create your models here.
class Expense(models.Model):
    amount = models.FloatField()
    vendor = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
