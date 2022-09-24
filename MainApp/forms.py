import datetime
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
import uuid
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox


class BlogCommentForm(forms.ModelForm):
    class Meta:
        model = BlogComments
        fields = ['name', 'email', 'body']
        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'cols': 2}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }


class ContactUsCommentForm(forms.ModelForm):
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)

    class Meta:
        model = ContactUsModel
        fields = ['name', 'email', 'body', 'captcha']
        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control', 'rows': 10, 'cols': 2}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'})
        }


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.is_active = False
        if commit:
            user.save()
            emailverification = EmailVerification()
            emailverification.user = user
            emailverification.activation_key = str(uuid.uuid4())
            emailverification.key_expires = datetime.datetime.now() + datetime.timedelta(days=2)
            emailverification.save()
        return user


class UserUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


# Profiele Update Form
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = ProfileImage
        fields = ['image']
