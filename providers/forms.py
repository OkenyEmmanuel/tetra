from django import forms
from datetime import datetime, timedelta

class RegistrationForm(forms.Form):
    username = forms.CharField(label='Firstname', max_length=100)
    lastname = forms.CharField(label='Lastname', max_length=100)
    email = forms.EmailField(label='Email')
    tel = forms.CharField(label='Telephone Number', max_length=15)
    gender = forms.ChoiceField(label='Gender', choices=(('male', 'Male'), ('female', 'Female')))
    dob = forms.DateField(label='Date of Birth')
    address = forms.CharField(label='Address', widget=forms.Textarea)
    dob1 = forms.DateField(label='Date Of Appointment')
    dob3 = forms.TimeField(label='Time of Appointment')
    appointment = forms.ChoiceField(label='Reason for Appointment', choices=(
        ('Medical Checkup', 'Medical Checkup'),
        ('Doctor Appointment', 'Doctor Appointment'),
        ('Medical Consultation', 'Medical Consultation'),
        ('Blood Test', 'Blood Test'),
    ))

    def clean_dob(self):
        dob = self.cleaned_data['dob']
        today = datetime.now().date()
        min_dob = today - timedelta(days=365 * 20)  # 20 years ago from today
        if dob >= today or dob <= min_dob:
            raise forms.ValidationError("Please enter a valid date of birth (should be at least 20 years old and in the past).")
        return dob

    def clean_dob1(self):
        dob1 = self.cleaned_data['dob1']
        today = datetime.now().date()
        if dob1 <= today:
            raise forms.ValidationError("Please select a date of appointment in the future.")
        return dob1
