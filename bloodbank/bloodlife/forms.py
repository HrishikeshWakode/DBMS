from django import forms
from .models import Hospital, User, Inventory

class HospitalForm(forms.ModelForm):
    class Meta:
        model = Hospital
        fields = ['name', 'location', 'contact_number', 'email']

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'phone', 'password_hash', 'role', 'hospital']

class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ['blood_group', 'units_available']
