from django.db import models

class Answer(models.Model):
    ess_gender = models.CharField(max_length=1)
    ess_age = models.CharField(max_length=1)
    ess_marital = models.CharField(max_length=1)
    ess_job = models.CharField(max_length=1)
    province = models.CharField(max_length=1)
    city = models.CharField(max_length=1)
    prefer = models.CharField(max_length=1)
    frequency = models.CharField(max_length=1)
    wineFrequency = models.CharField(max_length=1)
    side = models.CharField(max_length=1)
    area_grade = models.CharField(max_length=1)
    choice2 = models.CharField(max_length=1)


# Create your models here.
