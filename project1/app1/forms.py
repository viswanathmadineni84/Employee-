from django import forms
from app1.models import Employee,LatestNews,AddCalender


class EmployeeForm(forms.ModelForm):
    class Meta:
         model=Employee
         fields='__all__' 

class LatestNewsForm(forms.ModelForm):
    class Meta:
        model=LatestNews
        fields='__all__'

class AddCalenderForm(forms.ModelForm):
    class Meta:
        model=AddCalender
        fields='__all__'
            