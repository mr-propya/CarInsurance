# Generated by Django 2.2.4 on 2019-10-22 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('androidApis', '0002_remove_transactions_car'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='uid',
            new_name='username',
        ),
        migrations.AddField(
            model_name='customer',
            name='password',
            field=models.CharField(default='userName', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transactions',
            name='premiumId',
            field=models.IntegerField(default=50),
            preserve_default=False,
        ),
    ]