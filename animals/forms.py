from django import forms
from .models import Animal, Adoption

class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ['name', 'age', 'breed', 'description', 'photo', 'health_status']

class AdoptionForm(forms.ModelForm):
    class Meta:
        model = Adoption
        fields = ['animal', 'adopter_name', 'adoption_date']