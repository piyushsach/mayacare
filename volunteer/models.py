from django.db import models
from django.contrib.auth.models import User

TEAM_CHOICES = [
    ('P', 'Power Team'),
    ('V', 'Voice Team'),
    ('D', 'Data Team'),
]

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    team = models.CharField(max_length=1, choices=TEAM_CHOICES)
    special_ability = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    city = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    postal_code = models.CharField(max_length=6)
    aadharUID = models.IntegerField(null=True)
    def __str__(self):
        return f'{self.user.username} - {self.team}'


class TimeSheets(models.Model):
    volunteer = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.CharField(max_length=100)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    
    def __str__(self):
        return f'{self.volunteer.first_name}  {self.task}'