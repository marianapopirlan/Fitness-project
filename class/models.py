from django.db import models


class Class(models.Model):
    id = models.CharField(max_length=13, primary_key=True)
    name = models.CharField(max_length=30)
    date = models.DateTimeField("Date")
    trainer = models.CharField(max_length=20)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name + " cu " + self.trainer
