# Generated by Django 3.1.4 on 2021-02-04 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20210203_2130'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='group',
        ),
    ]
