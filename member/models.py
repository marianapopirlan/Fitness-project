from django.db import models
from django.utils import timezone


class Member(models.Model):
    cnp = models.CharField(max_length=13, primary_key=True)
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=20)
    date_of_birth = models.DateTimeField("Date Of Birth")
    join_date = models.DateTimeField("Date of Join")
    expiry_date = models.DateTimeField("Expiry date")

    def __str__(self):
        return self.name

    def membership_expired(self):
        return self.expiry_date <= timezone.now() # - datetime.timedelta(days=1)