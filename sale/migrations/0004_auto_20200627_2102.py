# Generated by Django 3.0.7 on 2020-06-27 21:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sale', '0003_report'),
    ]

    operations = [
        migrations.RenameField(
            model_name='report',
            old_name='company_name',
            new_name='name',
        ),
    ]
