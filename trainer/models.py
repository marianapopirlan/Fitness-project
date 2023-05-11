from django.db import models


class Trainer(models.Model):
    cnp = models.CharField(max_length=13, primary_key=True)
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=20)
    date_of_birth = models.DateField("Date of birth")
    speciality = models.CharField(max_length=20)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name
