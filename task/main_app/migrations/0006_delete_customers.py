# Generated by Django 4.1.7 on 2023-04-06 11:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_rename_customer_customers'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Customers',
        ),
    ]
