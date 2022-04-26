from django import forms
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
        # labels= {'address':'Location Address'}
        fields = ['address', 'lat', 'lng', 'google_id']

class Item_Form(ModelForm):

    perishable = forms.CheckboxInput()
    refrigeration = forms.CheckboxInput()
    has_item = forms.CheckboxInput()


    class Meta:
        model= Item
        help_texts= {'is_requested': 'Current Items are items donated to the pantry.\nRequested Items are items the pantry needs the most rigth now.'}
        labels= {'name': 'Item Name', 'best_by': 'Best by Date', 'quantity': 'Quantity', 'perishable': 'Is it Perishable?', 'refrigeration': 'Is Refrigeration needed?', 'is_requested': 'Needed?', 'keywords': 'Keywords'}
        fields = ['name', 'best_by', 'quantity', 'perishable', 'refrigeration', 'is_requested', 'keywords']