from django import forms
from .models import Comment

class AddCommentForm(forms.ModelForm):
    comment=forms.CharField(widget=forms.Textarea(attrs={'rows':4}))
    class Meta:
        model=Comment
        fields=('comment','stars_given')
