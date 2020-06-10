from django import forms

from .models import Reviews

class Reviews(forms.ModelForm):
    """Form review"""
    class Meta(Reviews):
        model = Reviews
        fields = ("name", "email", "text")