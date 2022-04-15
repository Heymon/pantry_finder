from django.shortcuts import render
from user_app.forms import User_Form
from .forms import Pantry_Form, Location_Form
# Create your views here.

def home(request):
    user_form = User_Form
    pantry_form = Pantry_Form
    location_form = Location_Form
    context = {'user_form': user_form, 'pantry_form': pantry_form, 'location_form': location_form}
    return render(request,'home.html', context)