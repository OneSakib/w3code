from django import forms
from .models import *


class JqueryCommentsForm(forms.ModelForm):
    class Meta:
        model = JqueryComments
        fields = ['name', 'email', 'body']
        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'cols': 2}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }


class AngularjsCommentsForm(forms.ModelForm):
    class Meta:
        model = AngularjsComments
        fields = ['name', 'email', 'body']
        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'cols': 2}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }


class NodejsCommentsForm(forms.ModelForm):
    class Meta:
        model = NodejsComments
        fields = ['name', 'email', 'body']
        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'cols': 2}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }


class ExpressjsCommentsForm(forms.ModelForm):
    class Meta:
        model = ExpressjsComments
        fields = ['name', 'email', 'body']
        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'cols': 2}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }


class ReactjsCommentsForm(forms.ModelForm):
    class Meta:
        model = ReactjsComments
        fields = ['name', 'email', 'body']
        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'cols': 2}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }


class TypeScriptsCommentsForm(forms.ModelForm):
    class Meta:
        model = TypeScriptsComments
        fields = ['name', 'email', 'body']
        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'cols': 2}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }


class VUEjsCommentsForm(forms.ModelForm):
    class Meta:
        model = VUEjsComments
        fields = ['name', 'email', 'body']
        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'cols': 2}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }
