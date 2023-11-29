from django import forms
from car.models import User

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'useremail', 'userphone', 'userpassword']
        widgets = {
            'userpassword': forms.PasswordInput(attrs={'placeholder': 'Password'}),
            'username': forms.TextInput(attrs={'placeholder': 'Your Name'}),
            'useremail': forms.EmailInput(attrs={'placeholder': 'Your Email'}),
            'userphone': forms.TextInput(attrs={'placeholder': 'Your Phone'}),
        }
