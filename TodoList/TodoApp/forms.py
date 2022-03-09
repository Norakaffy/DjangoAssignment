from dataclasses import fields
from django.forms import ModelForm
from.models import *


class TodoListForm(ModelForm):
    class Meta:
        model = Todolist
        exclude = ['datetime']
