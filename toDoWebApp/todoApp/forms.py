from django.forms import ModelForm
from .models import TodoList
from django import forms

class ToDoForm(ModelForm):
    task = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': "Add Todo"}))
    
    class Meta:
        model = TodoList
        fields = ['task']