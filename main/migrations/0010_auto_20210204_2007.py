# Generated by Django 3.1.4 on 2021-02-04 17:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20210204_2003'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clas',
            name='teacher',
        ),
        migrations.AddField(
            model_name='clas',
            name='teacher',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
