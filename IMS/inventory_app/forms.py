from django import forms
from .models import *

class hatchbackForm(forms.ModelForm):
    class Meta:
        model = hatchback
        fields = ('name', 'price', 'mileage', 'stock', 'wait_time')


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
