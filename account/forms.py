from django import forms
from .models import CustomUser
from django.contrib.auth.forms import PasswordChangeForm
class EditAccountForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['name','email', 'img']





