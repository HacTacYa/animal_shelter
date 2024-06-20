from django.db import models

class Animal(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    breed = models.CharField(max_length=100)
    description = models.TextField()
    photo = models.ImageField(upload_to='animals/')
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