from multiprocessing import context
from django.http import QueryDict
from django.shortcuts import redirect, render
from user_app.forms import User_Form
from .forms import Pantry_Form, Location_Form

from django.contrib.auth.forms import AuthenticationForm
# Create your views here.

def home(request):
    user_form = User_Form
    pantry_form = Pantry_Form
    location_form = Location_Form
    context = {'pantries': pantries,'user_form': user_form, 'pantry_form': pantry_form, 'location_form': location_form}
    return render(request,'home.html', context)

def user_auth(request):
    signup_form = User_Form
    login_form = AuthenticationForm

    if request.method == 'POST':
        print(request.POST)
        if request.POST.__getitem__('form') == 'signup':
            auth_form = User_Form(data=request.POST)
            if auth_form.is_valid():
                #TODO save; go to pantry form
                print('valid')
                return redirect('pantry_creation', user_id=1)
            else:
                context = {'signup_form': auth_form, 'login_form': login_form}
                return render(request,'user_auth.html', context)
        if request.POST.__getitem__('form') == 'login':
            print(request.POST)
            auth_form = AuthenticationForm(data=request.POST)
            if auth_form.is_valid():
                #TODO authenticate; login; go to profile
                print('valid')
                return render(request, 'user_auth.html')
            else:
                context = {'signup_form': signup_form, 'login_form': auth_form}
                return render(request,'user_auth.html', context)
    else:
        context = {'signup_form': signup_form, 'login_form': login_form}
        return render(request,'user_auth.html', context)


def pantry_creation(request, user_id):

    pantry_form = Pantry_Form
    location_form = Location_Form

    # TODO if connection break or closed delete user thru user_id

    if request.method == 'POST':
        mutable_post = request.POST.copy()
        location = QueryDict(f'address={mutable_post.pop("address")[0]}&google_id={mutable_post.pop("google_id")[0]}&lat={mutable_post.pop("lat")[0]}&lng={mutable_post.pop("lng")[0]}')

        pantry_form = Pantry_Form(mutable_post)
        location_form = Location_Form(location)
        if pantry_form.is_valid() and location_form.is_valid():
            print('valid')
            return redirect('user_auth')
        else:
            context = {'pantry_form': pantry_form, 'location_form': location_form}
            return render(request, 'pantry_creation.html', context)
    else:
        context = {'pantry_form': pantry_form, 'location_form': location_form}
        return render(request, 'pantry_creation.html', context)


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
