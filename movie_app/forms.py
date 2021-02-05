from django import forms
from .models import MovieInfo,Review

class MovieResForms(forms.ModelForm):
    class Meta:
        model=MovieInfo
        fields='__all__'

class RatingForms(forms.ModelForm):
    class Meta:
        model=Review
        fields='__all__'
