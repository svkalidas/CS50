from django import forms


class TaskForm(forms.Form):
    task = forms.CharField(label="New Task")