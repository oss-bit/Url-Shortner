from django.contrib.auth.forms import UserCreationForm
from django.forms import DateInput, TextInput, PasswordInput
from .models import RUser


class RUserCreationForm(UserCreationForm):
    class Meta:
        model = RUser
        fields = ['name','email', 'DoB', 'password1', 'password2']        
        widgets = {
            'name' : TextInput(attrs={
                "class" : "form-control",
                "style" : "width: 300px;",
                "placeholder": "Input your name"
            }),
            #
            'password1': PasswordInput(attrs={
                "class":"form-control",
                "style": "width: 300px;",
                "type": "password",
            }),
            'password2': PasswordInput(attrs={
                "class": "form-control",
                "style": "width: 300px;",
                "type": "password",
            }),

        }