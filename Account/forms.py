from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm




class LoginForm(forms.Form):
    username= forms.CharField(max_length=100,label="",widget=forms.TextInput(attrs={"class":" form-control w-100 field mb-3 mt-5 rounded border-top-0 border-left-0 border-right-0 border-bottom ","placeholder":"Username"}))
    password = forms.CharField(max_length=100, label="",widget=forms.PasswordInput(attrs={"class":"form-control field mb-5   rounded border-top-0 border-left-0 border-right-0 border-bottom","placeholder":"Password"}))

class NewUser(UserCreationForm):
    # is_staff=
    class Meta:
        model=User
        fields = ["first_name","last_name","email","username","password1","password2","is_staff"]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['is_staff'].label = 'Are you a Dealer'
        self.fields['is_staff'].help_text = 'If you want to Login as Dealer Please Tick this field.\n Otherwise Leave this Field'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Loop through all fields and add a CSS class to each field's widget
        for field_name, field in self.fields.items():
            if field_name != 'is_staff':
                field.widget.attrs.update({
                    'class': 'form-control'
                })

    
        self.fields['is_staff'].label = 'Are you a Dealer'
        self.fields['is_staff'].help_text = 'If you want to Login as Dealer Please Tick this field.\n Otherwise Leave this Field'
    