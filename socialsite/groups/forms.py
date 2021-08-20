from django.contrib.auth.models import User
from .models import Groups
from posts.models import Posts
from django import forms


class GroupCreateForm(forms.ModelForm):
    class Meta:
        model = Groups
        fields = ('user', 'cover_pic', 'groups_name', 'type_group', 'about_group')

        widgets = {
                'user': forms.TextInput(attrs={'class': 'form-control', 'value':'', 'id':'groupuser', 'type': 'hidden'}),
            }

    groups_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control input-group-text',
        'type':'text',
        'placeholder': 'Enter the group name..'
    }), label='Group Name')


    type_group = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control input-group-text',
        'type':'text',
        'placeholder': 'Enter type of group..'
    }), label='Type Group')

    about_group = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control input-group-text',
        'type':'text',
        'placeholder': 'Enter the about group..'
    }), label='About Group')


class GroupUpdateForm(forms.ModelForm):
    class Meta:
        model = Groups
        fields = ('cover_pic', 'groups_name', 'type_group', 'about_group')



    groups_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control input-group-text',
        'type':'text',
        'placeholder': 'Enter the group name..'
    }), label='Group Name')


    type_group = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control input-group-text',
        'type':'text',
        'placeholder': 'Enter type of group..'
    }), label='Type Group')

    about_group = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control input-group-text',
        'type':'text',
        'placeholder': 'Enter the about group..'
    }), label='About Group')


class GroupPostCreateForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ('post_body', 'post_image')


    post_body = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control input-group-text',
        'type':'text',
        'placeholder': 'Whats on your mind..'
    }), label='Message')
