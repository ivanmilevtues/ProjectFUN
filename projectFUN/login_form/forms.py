from django import forms
import hashlib

from login_form.models import User


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password', 'username']
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


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput, max_length=128)

    def clean_password(self):
        password = hashlib.sha512(self.cleaned_data['password'].encode())\
                          .hexdigest()
        return password

    def find(self, commit=True):
        u = User.objects.filter(email=self.cleaned_data['email'],
                                password=self.cleaned_data['password']).first()
        return u
