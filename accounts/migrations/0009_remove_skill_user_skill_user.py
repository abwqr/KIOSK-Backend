# Generated by Django 4.1.5 on 2023-01-29 20:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_remove_skill_user_skill_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skill',
            name='user',
        ),
        migrations.AddField(
            model_name='skill',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='skill', to=settings.AUTH_USER_MODEL),
        ),
    ]
