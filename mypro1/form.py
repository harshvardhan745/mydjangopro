from dataclasses import fields

from django.forms import forms

from mypro1.models import Employee

'''class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '_all_'
'''


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        #fields = "_all_"
        fields = ('name', 'email')
