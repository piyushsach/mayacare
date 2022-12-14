from django.db import models

# Create your models here.
class Donation(models.Model):
    donor_name = models.CharField(max_length=30)
    transaction_id = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f'{self.donor_name} - {self.amount}'