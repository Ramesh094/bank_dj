# Generated by Django 4.2.6 on 2023-10-18 07:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newb', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounts',
            name='aadhar',
            field=models.IntegerField(max_length=12, validators=[django.core.validators.RegexValidator(message='Your Aadhar number should be 12 digits long', regex='^\\d{12}$')]),
        ),
        migrations.AlterField(
            model_name='accounts',
            name='mobile',
            field=models.IntegerField(max_length=10, validators=[django.core.validators.RegexValidator(message='Your mobile number should be 10 digits long', regex='^\\d{10}$')]),
        ),
    ]
