from django import forms

from .models import Student


class StudentCreateForms(forms.ModelForm):

    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'age', 'birthday']
        widgets = {'birthday': forms.DateInput(attrs={'type': 'date'})}

    # cleaned_date
    def clean_first_name(self):
        data = self.cleaned_data["first_name"]
        return data.title()

    def clean_last_name(self):
        data = self.cleaned_data["last_name"]
        return data.title()
