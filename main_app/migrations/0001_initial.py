# Generated by Django 3.1.5 on 2022-04-14 02:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('best_by', models.DateField(blank=True, verbose_name='Best By')),
                ('quantity', models.IntegerField(default=1)),
                ('perishable', models.BooleanField(default=True)),
                ('refrigeration', models.BooleanField(default=False)),
                ('has_item', models.BooleanField(default=True)),
                ('keywords', models.TextField(blank=True, max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=100)),
                ('lat', models.FloatField()),
                ('lng', models.FloatField()),
                ('google_id', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Pantry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('email', models.EmailField(max_length=350, validators=[django.core.validators.RegexValidator(code='Invalid Email Format', message='EX: address@domain.com', regex='^\\w.{1,64}@\\w.{1,253}\\.\\w*$')])),
                ('phone', models.CharField(max_length=16, validators=[django.core.validators.RegexValidator(code='Invalid Phone Format', message='EX: +# ###-###-####', regex='^(\\+?\\d{1,2}\\s?)?\\(?\\d{3}\\)?[\\s.-]?\\d{3}[\\s.-]?\\d{4}$')])),
                ('description', models.TextField(blank=True, max_length=1000)),
            ],
        ),
    ]