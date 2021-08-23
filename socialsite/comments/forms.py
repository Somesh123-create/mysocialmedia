from django.contrib.auth.models import User
from .models import Comments, CommentReply
from django import forms


class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('body',)

    body = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control input-group-text',
        'type':'text',
        'height':15,
        'rows':2,
        'cols':15,
        'placeholder': 'Enter the comment..'
    }), label='')

class CommentUpdateForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('body',)

    body = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control input-group-text',
        'type':'text',
        'height':15,
        'rows':2,
        'cols':15,
        'placeholder': 'Enter the comment..'
    }), label='')


class CommentReplyForm(forms.ModelForm):
    class Meta:
        model = CommentReply
        fields = ('comment','replay',)

    replay = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control input-group-text',
        'type':'text',
        'height':15,
        'rows':2,
        'cols':25,
        'placeholder': 'Enter the comment..'
    }), label='')
