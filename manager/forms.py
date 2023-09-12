from Account.models import Property

from django import forms

class PropertyForm(forms.ModelForm):
    class Meta:
        model=Property
        fields="__all__"
        widgets={
            "place":forms.TextInput(attrs={"class":"form-control","name":'new'}),
            "district":forms.Select(attrs={"class":"form-control"}),
            "cent":forms.NumberInput(attrs={"class":"form-control"}),
            "building":forms.CheckboxInput(),
            "price":forms.NumberInput(attrs={"class":"form-control"}),
            "img1":forms.FileInput(attrs={"class":"form-control"}),
            "img2":forms.FileInput(attrs={"class":"form-control"}),
            "img3":forms.FileInput(attrs={"class":"form-control"}),
            
            "descripton":forms.Textarea(attrs={"class":"form-control","placeholder":"enter descriptn"}),
            
        }
        labels = {
            'place': 'Enter Place of property',
            'district': 'Enter district ',
        }