from main_app.models import Pantry, Location, Item
from django.forms import ModelForm


class Pantry_Form(ModelForm):
    
    class Meta:
        model= Pantry
        labels= {'name':'Location Name', 'email': 'Contact Email', 'phone': 'Contact Phone', 'description': 'Information'}
        fields = ['name', 'email', 'phone', 'description']

class Location_Form(ModelForm):
    
    class Meta:
        model= Location
        labels= {'address':'Location Address'}
        fields = ['address']