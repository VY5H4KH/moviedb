from django import forms
from .models import Review

class Movieform(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['Name','Mail_id','Your_Review']
        widgets = {
            'Your_Review': forms.Textarea(attrs={'rows': 3}),
        }