from django.db import models
from django.utils import timezone

class Animal(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    breed = models.CharField(max_length=100)
    description = models.TextField()
    health_status = models.CharField(max_length=100)
    is_adopted = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Adoption(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    adopter_name = models.CharField(max_length=100)
    adoption_date = models.DateField()

    def __str__(self):
        return f"{self.adopter_name} adopted {self.animal.name}"
    
class Employee(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return self.name

class Feed(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Account(models.Model):
    account_number = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    total_donations = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    
class Donation(models.Model):
    donor_name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.donor_name} - {self.amount}"