from django import forms
from BUCKDJANGOAPP.models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'rollNo', 'email', 'contact']
