from .models import Myid
from django.forms import ModelForm,TextInput,DateTimeInput,CharField



class MyidForm(ModelForm):
    class Meta:
        model = Myid
        fields = ['name_company','culture','price','date','idcheck']

        widgets = {
            "name_company":TextInput(attrs={
                'class':'form-control',
                'placeholder':'Назва компанії'
            }),

            "culture": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Культура'
            }),

            "price": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ціна'
            }),

            "date": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата'
            }),

            "idcheck": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ID'

            })

        }