# Generated by Django 2.2.4 on 2019-09-04 18:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('androidApis', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transactions',
            name='car',
        ),
    ]