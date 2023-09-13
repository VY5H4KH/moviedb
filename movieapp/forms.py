from django import forms
from .models import Review

class Movieform(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rev_name','rev_mail','rev_con']