from . import models
from django import forms
from datetime import date, datetime

def validate_date(date_text):
    """
    validates if the date follows the YYYY-MM-DD format
    """
    try:
        datetime.strptime(date_text, '%Y-%m-%d')
    except ValueError:
        raise forms.ValidationError("Incorrect date format, should be YYYY-MM-DD")

class LeaveForm(forms.ModelForm):
    class Meta:
        model = models.Leave
        fields = ['leave_type', 'start_date', 'end_date', 'user']

    def clean(self):
        validate_date(self.data['start_date'])
        validate_date(self.data['end_date'])
        today = date.today()
        start_date = self.cleaned_data['start_date']
        end_date = self.cleaned_data['end_date']   

        if today > start_date or today > end_date:
            raise forms.ValidationError("Start date and end date must be a future date")                                                                         

        if end_date <= start_date:
            raise forms.ValidationError("End date must be later than start date")
        return super(LeaveForm, self).clean()

class UserForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ['name']

    def clean(self):
        if len(self.data['name']) > 50:
            raise forms.ValidationError("Name must be less than 50 characters")