from django import forms
from .models import Departments
class DepartmentForm(forms.Form):
    name = ""
    description = "Use the dropdown to select an arena."
    selections = forms.ChoiceField(choices=Departments.objects.values_list('id','nom'),
                                  widget=forms.Select(),required=True)