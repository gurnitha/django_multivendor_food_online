# app/vendors/forms.py

# Django modules
from django import forms

# locals
from app.vendors.models import Vendor

class VendorRegistrationForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = ['vendor_name', 'vendor_license']
