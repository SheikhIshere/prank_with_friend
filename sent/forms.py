# forms.py

from django import forms
from .models import SentModel

class SentForm(forms.ModelForm):
    class Meta:
        model = SentModel
        fields = ['sent_address']
        widgets = {
            'sent_address': forms.EmailInput(attrs={'placeholder': 'recipient@example.com', 'class': 'border p-2 rounded w-full'}),
        }




# www.shaoyn111@gmail.com