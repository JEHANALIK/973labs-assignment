# Generated by Django 4.1.7 on 2023-04-06 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='pic',
            field=models.ImageField(blank=True, upload_to='main_app/static/uploads/'),
        ),
    ]
