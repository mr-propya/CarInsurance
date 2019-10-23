# Generated by Django 2.2.4 on 2019-10-23 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('androidApis', '0004_car_claims'),
    ]

    operations = [
        migrations.RenameField(
            model_name='insurance',
            old_name='dateOfInsurance',
            new_name='boughtAt',
        ),
        migrations.RenameField(
            model_name='insurance',
            old_name='monthlyPremium',
            new_name='premium',
        ),
        migrations.AlterField(
            model_name='insurance',
            name='balance',
            field=models.FloatField(default=0),
        ),
    ]