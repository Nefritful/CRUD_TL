# Generated by Django 4.2.1 on 2023-10-24 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='level',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
