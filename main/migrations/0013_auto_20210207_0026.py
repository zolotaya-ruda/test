# Generated by Django 3.1.4 on 2021-02-06 21:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20210205_1632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clas',
            name='teacher',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]