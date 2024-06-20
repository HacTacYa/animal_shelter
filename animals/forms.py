from django import forms
from .models import Animal, Adoption, Employee, Feed, Account, Donation

class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ['name', 'age', 'breed', 'description', 'health_status']
        labels = {
            'name': 'Кличка',
            'age': 'Возраст',
            'breed': 'Вид',
            'description': 'Описание',
            'health_status': 'Состояние здоровья',
        }
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }
        
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['photo'].widget.attrs.update({'accept': 'image/*'})


class AdoptionForm(forms.ModelForm):
    class Meta:
        model = Adoption
        fields = ['animal', 'adopter_name', 'adoption_date']
        
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'position', 'bio']
        labels = {
            'name': 'ФИО',
            'position': 'Должность',
            'bio': 'Информация',
        }

class FeedForm(forms.ModelForm):
    class Meta:
        model = Feed
        fields = ['name', 'description']
        labels = {
            'name': 'Название корма',
            'description': 'Описание',
        }

class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['account_number', 'balance']
        labels = {
            'account_number': 'ФИО',
            'balance': 'Сумма',
        }
        
class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = '__all__'