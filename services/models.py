from django.db import models
from volunteer.models import Profile

GENDER_CHOICES = [
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other'),
]


# Create your models here.
class Beneficiary(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    city = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    postal_code = models.CharField(max_length=6)
    phone = models.CharField(max_length=10)
    
    def __str__(self):
        return f'{self.first_name}'
    
    
class Service(models.Model):
    issue_faced = models.TextField()
    special_requests = models.TextField()
    volunteer_id = models.ForeignKey(Profile, on_delete=models.DO_NOTHING, null=True)
    beneficiary_id = models.ForeignKey(Beneficiary, on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return f'{self.issue_faced} - {self.beneficiary_id.first_name}'