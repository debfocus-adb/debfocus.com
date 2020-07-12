# Generated by Django 3.0.7 on 2020-06-27 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sale', '0002_auto_20200627_2007'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=200)),
                ('statement', models.TextField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Report',
            },
        ),
    ]