from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    completed = forms.BooleanField(required=False)  # チェックボックスのフィールドを追加
    
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'priority', 'category', 'completed']
