# Generated by Django 3.1 on 2020-08-13 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customuser', '0004_user_is_invited_person'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='temp_password',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='temp_password'),
        ),
    ]
