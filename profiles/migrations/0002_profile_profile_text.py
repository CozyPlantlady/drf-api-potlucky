# Generated by Django 3.2.16 on 2022-12-19 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_text',
            field=models.TextField(blank=True, max_length=1000),
        ),
    ]