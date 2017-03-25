from django import forms
import hashlib

from login_form.models import User


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        labels = {
            'email': 'Email:',
            'password': 'Password:',
            'username': 'Username:',
        }
        widgets = {
            'password': forms.PasswordInput()
        }

    def clean_password(self):
        password = hashlib.sha512(self.cleaned_data['password'].encode())\
                          .hexdigest()
        return password
