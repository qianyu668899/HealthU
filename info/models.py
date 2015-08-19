from django.db import models
from decimal import Decimal

# Create your models here.
class PersonBasic(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    email = models.EmailField(max_length = 70)

class PersonHealth(models.Model):
    person = models.ForeignKey(PersonBasic)
    dateOfBirth = models.DateField()
    height = models.DecimalField(max_digits=20, decimal_places=2, default=Decimal('0.00'))
    weight = models.DecimalField(max_digits=20, decimal_places=2, default=Decimal('0.00'))
