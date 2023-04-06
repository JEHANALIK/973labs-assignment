# Generated by Django 4.1.7 on 2023-04-06 11:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_delete_customers'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=265)),
                ('path', models.CharField(max_length=100)),
                ('action', models.CharField(max_length=100)),
                ('error', models.CharField(max_length=100)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.client')),
            ],
        ),
    ]