from django import forms
from .models import CustomUser

class EditAccountForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['name', 'age', 'email', 'role', 'img']
