
from django import forms

from.models import movie
class Movie_form(forms.ModelForm):
    class Meta:
        model=movie
        fields=['name','desc','year','image']