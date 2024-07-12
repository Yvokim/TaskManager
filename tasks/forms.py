from django import forms
from .models import Task
from .models import Subtask


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'deadline',   'status', 'assigned_to']


class SubTaskForm(forms.ModelForm):
    class Meta:
        model = Subtask
        fields = ['task', 'title', 'description', 'due_date', 'is_completed']
