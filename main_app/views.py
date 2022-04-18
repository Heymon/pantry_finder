from django.shortcuts import render
from user_app.forms import User_Form
from .forms import Pantry_Form, Location_Form
# Create your views here.

def home(request):
    user_form = User_Form
    pantry_form = Pantry_Form
    location_form = Location_Form
    context = {'pantries': pantries,'user_form': user_form, 'pantry_form': pantry_form, 'location_form': location_form}
    return render(request,'home.html', context)

class Location:

    def  __init__(self, address, lat, lng ):
        self.address = address
        self.lat = lat
        self.lng = lng

class Pantry:

    def __init__(self, id, title, location, contact, description ):
        self.id = id
        self.title = title
        self.location = location
        self.contact = contact
        self.description = description

pantries = [
    Pantry(#
        "1D",#id
        "San Francisco", #charField
        Location("San Francisco, CA, USA", 37.77514760291072, -122.41941013558197),#charField, integerField
        "415-975-4767",#charField 
        "Only has ham"#textField
        ),
    Pantry(
        "2D",
        "Ocean Beach", 
        Location("Ocean Beach, San Francisco, CA, USA", 37.75971813007669, -122.51073936441803),
        "415-975-4767",
        "NO HAMS ALLOWED"
        ),
    Pantry(
        "3D",
        "Community Fridge and Cabinet", 
        Location("20324 Forest Ave, Castro Valley, CA 94546", 37.69752069616992, -122.06889211536156),
        "NOT AVAILABLE",
        "Community Organized"
        ),
    Pantry(#
        "1D",#id
        "San Francisco", #charField
        Location("San Francisco, CA, USA", 37.77514760291072, -122.41941013558197),#charField, integerField
        "415-975-4767",#charField 
        "Only has ham"#textField
        ),
    Pantry(
        "2D",
        "Ocean Beach", 
        Location("Ocean Beach, San Francisco, CA, USA", 37.75971813007669, -122.51073936441803),
        "415-975-4767",
        "NO HAMS ALLOWED"
        ),
    Pantry(
        "3D",
        "Community Fridge and Cabinet", 
        Location("20324 Forest Ave, Castro Valley, CA 94546", 37.69752069616992, -122.06889211536156),
        "NOT AVAILABLE",
        "Community Organized"
        ),
    Pantry(#
        "1D",#id
        "San Francisco", #charField
        Location("San Francisco, CA, USA", 37.77514760291072, -122.41941013558197),#charField, integerField
        "415-975-4767",#charField 
        "Only has ham"#textField
        ),
    Pantry(
        "2D",
        "Ocean Beach", 
        Location("Ocean Beach, San Francisco, CA, USA", 37.75971813007669, -122.51073936441803),
        "415-975-4767",
        "NO HAMS ALLOWED"
        ),
    Pantry(
        "3D",
        "Community Fridge and Cabinet", 
        Location("20324 Forest Ave, Castro Valley, CA 94546", 37.69752069616992, -122.06889211536156),
        "NOT AVAILABLE",
        "Community Organized"
        ),

]
