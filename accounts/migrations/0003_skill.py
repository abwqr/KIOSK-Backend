# Generated by Django 4.1.5 on 2023-01-28 09:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_skill_user_delete_education_delete_skill'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_name', models.CharField(default=' ', max_length=30, unique=True)),
                ('skill_description', models.TextField(null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='skill', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
