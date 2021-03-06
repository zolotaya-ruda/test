# Generated by Django 3.1.4 on 2021-02-11 17:45

import django.contrib.auth.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_auto_20210207_0030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='first_name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='last_name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='username',
            field=models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username'),
        ),
    ]
