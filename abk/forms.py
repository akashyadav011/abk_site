from django import forms
from .models import Enquiry

class EnquiryForm(forms.ModelForm):
    class Meta:
        model = Enquiry
        fields = ['name', 'email', 'phone', 'message', 'product']
        widgets = {
            'product': forms.HiddenInput()
        }
