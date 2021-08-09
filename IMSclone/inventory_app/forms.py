from django import forms # Django already provides us with ModelForms
from .models import *
# forms are required to enter information into our database

class hatchbackForm(forms.ModelForm): # inheritance
    class Meta:
        model = hatchback
        fields = ('name', 'price', 'mileage', 'stock', 'wait_time') # fields as defined in models


class sedanForm(forms.ModelForm):
    class Meta:
        model = sedan
        fields = ('name', 'price', 'mileage', 'stock', 'wait_time')


class SUVMUVForm(forms.ModelForm):
    class Meta:
        model = SUVMUV
        fields = ('name', 'price', 'mileage', 'stock', 'wait_time')

class vanForm(forms.ModelForm):
    class Meta:
        model = van
        fields = ('name', 'price', 'mileage', 'stock', 'wait_time')

# will be used in our HTML as <form> </form>