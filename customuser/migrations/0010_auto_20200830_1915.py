# Generated by Django 3.1 on 2020-08-30 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customuser', '0009_ratedstage2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='category',
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='First name'),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
