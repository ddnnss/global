# Generated by Django 3.1 on 2020-08-13 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_startup'),
    ]

    operations = [
        migrations.AddField(
            model_name='startup',
            name='original_id',
            field=models.IntegerField(default=0),
        ),
    ]