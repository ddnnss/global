# Generated by Django 3.1 on 2020-08-12 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customuser', '0002_rated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rated',
            name='startup',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
