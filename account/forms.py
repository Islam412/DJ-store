from django import forms
from .models import CustomUser
from django.contrib.auth.forms import PasswordChangeForm
class EditAccountForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['name', 'age', 'email', 'role', 'img']




class ChangePasswordForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['old_password'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Old Password'})
        self.fields['new_password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'New Password'})
        self.fields['new_password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Confirm New Password'})
