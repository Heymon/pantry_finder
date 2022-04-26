from django.db import models

# from django.contrib.auth.models import User

from user_app.models import User

from django.core.validators import RegexValidator
# Create your models here.

class Pantry(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=50, unique=True)
    email=models.EmailField(max_length=350,
        validators=[
            RegexValidator(
                    regex='^\w.{1,64}@\w.{1,253}\.\w*$',
                    message='EX: address@domain.com',
                    code="Invalid Email Format"
                    )])
    phone=models.CharField(max_length=16,
        validators=[
            RegexValidator(
                regex='^(\+?\d{1,2}\s?)?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$',
                message='EX: +# ###-###-####',
                code="Invalid Phone Format"
                )])
    description=models.TextField(max_length=1000, blank=True)

class Location(models.Model):
    pantry=models.OneToOneField(Pantry, on_delete=models.CASCADE)
    address=models.CharField(max_length=100)
    lat=models.FloatField()
    lng=models.FloatField()
    google_id=models.CharField(max_length=200)

class Item(models.Model):
    pantry=models.ForeignKey(Pantry, on_delete=models.CASCADE)
    name=models.CharField(max_length=50);
    best_by=models.DateField("Best By", auto_now=False, auto_now_add=False, blank=True)
    quantity=models.IntegerField(default=1)
    perishable=models.BooleanField(default=True)
    refrigeration=models.BooleanField(default=False)
    is_requested=models.BooleanField(default=False)
    keywords=models.TextField(max_length=300, blank=True)
    # keywords=ArrayField(base_field=models.CharField(max_length=10)


