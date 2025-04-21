from django import forms
from apps.dashboard.models import CRUD

class CRUDforms(forms.ModelForm):
    class Meta:
        model = CRUD
        fields = [
            'images', 'full_name', 'company_name', 'about_company',
            'website_company', 'linkedin_company', 'company_type',
            'office_address', 'contact_phone'
        ]
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your full name'
            }),
            'company_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Company name'
            }),
            'about_company': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Write something about your company...'
            }),
            'website_company': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://example.com'
            }),
            'linkedin_company': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'LinkedIn URL'
            }),
            'company_type': forms.Select(attrs={
                'class': 'form-control'
            }),
            'office_address': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 2,
                'placeholder': 'Office address'
            }),
            'contact_phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '+91 XXXXX-XXXXX'
            }),
            'images': forms.ClearableFileInput(attrs={
                'class': 'form-control-file'
            }),
        }
