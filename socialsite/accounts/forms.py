from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, UserChangeForm
from .models import Profile

from django import forms


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control input-group-text',
        'type':'text',
        'placeholder': 'Enter Username'
    }), label='Username')

    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control input-group-text',
        'type':'text',
        'placeholder': 'Enter First Name'
    }),)

    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control input-group-text',
        'type':'text',
        'placeholder': 'Enter Last Name'
    }), label='Last name')

    email = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control input-group-text',
        'type':'email',
        'placeholder': 'Enter Email'
    }), label='Email address')

    password1 = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control input-group-text',
        'type':'password',
        'placeholder': 'Enter Password'
    }), label='Password')

    password2 = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control input-group-text',
        'type':'password',
        'placeholder': 'Confirm Password'
    }), label='Confirm Password')




class UserPasswordChangeForm(PasswordChangeForm):
    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')


    old_password = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control input-group-text',
        'type':'password',
        'placeholder': 'Enter Old Password'
    }), label='Old Password')

    new_password1 = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control input-group-text',
        'type':'password',
        'placeholder': 'Enter New Password'
    }), label='New Password')

    new_password2 = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control input-group-text',
        'type':'password',
        'placeholder': 'Confirm Password'
    }), label='Confirm Password')






class UserSettingsEditForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control input-group-text',
        'type':'text',
        'placeholder': 'Enter Username'
    }), label='Username')

    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control input-group-text',
        'type':'text',
        'placeholder': 'Enter First Name'
    }),)

    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control input-group-text',
        'type':'text',
        'placeholder': 'Enter Last Name'
    }), label='Last name')

    email = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control input-group-text',
        'type':'email',
        'placeholder': 'Enter Email'
    }), label='Email address')






class UserProfileCreateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('user', 'profile_pic', 'cover_pic', 'user_bio', 'designation', 'education', 'marital_status', 'hobbies', 'location', 'mobile')

    user = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control input-group-text',
        'type':'hidden',
        'value':'',
        'id':'somesh',
        'type': 'hidden',
    }))



class UserProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('profile_pic', 'cover_pic', 'user_bio', 'designation', 'education', 'marital_status', 'hobbies', 'location', 'mobile')


    user_bio = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control input-group-text',
        'type':'text'
    }), label='User Bio', required=False)

    designation = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control input-group-text',
        'type':'text'
    }), label='Designation')

    education = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control input-group-text',
        'type':'text'
    }), label='Education')

    marital_status = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control input-group-text',
        'type':'text'
    }), label='Marital Status')

    hobbies = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control input-group-text',
        'type':'text'
    }), label='Hobbies')

    location = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control input-group-text',
        'type':'text'
    }), label='Location')

    mobile = forms.IntegerField(widget=forms.TextInput(attrs={
        'class': 'form-control input-group-text',
        'type':'text'
    }), label='Mobile')
