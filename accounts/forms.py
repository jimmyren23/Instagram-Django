from django.forms import ModelForm, Textarea
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import *
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

class ResultsForm(ModelForm):
    class Meta:
        model = Post
        fields = ['content', 'post_pic']
        widgets = {
            'content': Textarea(attrs={'cols': 80, 'rows': 20}),
        }
class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': Textarea(attrs={'cols': 80, 'rows': 20}),
        }