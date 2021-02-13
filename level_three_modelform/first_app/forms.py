from django import forms
from .models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

    def clean(self):
        all_clean_data = super().clean()
        password = all_clean_data['password']
        confirm_password = all_clean_data['confirm_password']

        if password != confirm_password:
            raise forms.ValidationError('MAKE SURE passwords MATCH!')
