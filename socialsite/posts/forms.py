from django.contrib.auth.models import User
from .models import Posts
from django import forms


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ('post_body', 'post_image')



    post_body = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control input-group-text',
        'type':'text',
        'placeholder': 'Create post..'
    }), label='Post Body')
