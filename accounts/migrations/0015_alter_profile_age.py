# Generated by Django 4.1.5 on 2023-02-07 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_profile_age_profile_city_profile_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='age',
            field=models.PositiveIntegerField(default=None, null=True),
        ),
    ]
