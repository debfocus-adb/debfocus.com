from django import forms
from .models import Profile
from .models import Report

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        
        fields = ["company_name", "description","password", "phone", "email"]


class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        
        fields = ["name", "phone", "email", "statement"]