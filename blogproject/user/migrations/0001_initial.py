# Generated by Django 5.1 on 2024-09-03 11:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(error_messages={'unique': 'A user with this username already exists.'}, max_length=25, unique=True, validators=[django.core.validators.RegexValidator('^[a-zA-Z0-9_]+$', message='Username must contain only letters, numbers, or underscores.'), django.core.validators.MinLengthValidator(4, message='Username must be at least 4 characters long.')])),
                ('email', models.EmailField(error_messages={'unique': 'A user with this email address already exists.'}, max_length=30, unique=True, validators=[django.core.validators.MinLengthValidator(5, message='Email must be at least 5 characters long.')])),
                ('phone', models.CharField(blank=True, error_messages={'unique': 'A user with this phone number already exists.'}, max_length=12, null=True, unique=True, validators=[django.core.validators.MinLengthValidator(10, message='Phone number must be at least 10 characters long.')])),
                ('password', models.CharField(max_length=256)),
            ],
            options={
                'db_table': 'userinfo',
            },
        ),
    ]
