from django.db import models

# Create your models here.
class Data(models.Model):
    name = models.CharField(max_length=12)
    date_recorded = models.DateField(auto_now=True)
    