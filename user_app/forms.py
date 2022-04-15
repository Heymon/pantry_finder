from cProfile import label
from dataclasses import fields
from pyexpat import model
from django.contrib.auth.forms import UserCreationForm
from .models import User

class User_Form(UserCreationForm):

    class Meta:
        model = User
        labels = {'email': 'Email'}
        fields = ("email",)