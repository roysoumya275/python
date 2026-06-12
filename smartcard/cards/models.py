from django.db import models

# Create your models here.
class SmartCard(models.Model):
    name = models.CharField(max_length=50)
    card_number = models.CharField(max_length=12, unique=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name