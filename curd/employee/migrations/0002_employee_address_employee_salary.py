# Generated by Django 4.0.1 on 2022-01-25 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='address',
            field=models.CharField(blank=True, max_length=100, null=None),
        ),
        migrations.AddField(
            model_name='employee',
            name='salary',
            field=models.CharField(blank=True, max_length=10, null=None),
        ),
    ]
