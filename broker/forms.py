from Account.models import Broker

from django import forms

class BrokerForm(forms.ModelForm):
    class Meta:
        model=Broker
        fields="__all__"
        widgets={
            "Bname":forms.TextInput(attrs={"class":"form-control","placeholder":"Enter name"}),
            "Bplace":forms.TextInput(attrs={"class":"form-control","placeholder":"Enter name"}),
            "Bdistrict":forms.Select(attrs={"class":"form-control"}),
            "Bphone":forms.NumberInput(attrs={"class":"form-control","placeholder":"Enter phone"}),
            "Bage":forms.NumberInput(attrs={"class":"form-control","placeholder":"Enter phone"}),

    

        }