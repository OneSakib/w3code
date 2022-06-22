from django import forms
from .models import *


class MysqlDBCommentsForm(forms.ModelForm):
    class Meta:
        model = MysqlDBComments
        fields = ['name', 'email', 'body']
        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'cols': 2}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }


class MongoDBCommentsForm(forms.ModelForm):
    class Meta:
        model = MongoDBComments
        fields = ['name', 'email', 'body']
        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'cols': 2}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }


class PostgreSQLDBCommentsForm(forms.ModelForm):
    class Meta:
        model = PostgreSQLDBComments
        fields = ['name', 'email', 'body']
        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'cols': 2}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }


class SqliteDBCommentsForm(forms.ModelForm):
    class Meta:
        model = SqliteDBComments
        fields = ['name', 'email', 'body']
        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'cols': 2}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }


class OracleDBCommentssForm(forms.ModelForm):
    class Meta:
        model = OracleDBComments
        fields = ['name', 'email', 'body']
        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'cols': 2}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }


class MariaDBCommentsForm(forms.ModelForm):
    class Meta:
        model = MariaDBComments
        fields = ['name', 'email', 'body']
        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'cols': 2}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }
