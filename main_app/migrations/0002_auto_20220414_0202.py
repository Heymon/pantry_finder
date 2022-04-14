# Generated by Django 3.1.5 on 2022-04-14 02:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pantry',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='location',
            name='pantry',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main_app.pantry'),
        ),
        migrations.AddField(
            model_name='item',
            name='pantry',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.pantry'),
        ),
    ]