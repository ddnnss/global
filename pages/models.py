from django.db import models


class Startups(models.Model):
    order = models.CharField(max_length=32)
    approved = models.CharField(max_length=3)
    contest = models.CharField(max_length=250)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    position = models.CharField(max_length=250)
    company = models.CharField(max_length=250)
    website = models.CharField(max_length=250)
    linkedin = models.CharField(max_length=250)
    facebook = models.CharField(max_length=250)
    employees = models.CharField(max_length=250)
    stage = models.CharField(max_length=250)
    funding = models.CharField(max_length=250)
    video = models.CharField(max_length=250)
    idea = models.TextField()
    logo = models.CharField(max_length=250)
    presentation = models.CharField(max_length=250)
    date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'startups'


class StartUp(models.Model):
    original_id = models.IntegerField(default=0)
    order = models.CharField(max_length=32)
    approved = models.CharField(max_length=3)
    contest = models.CharField(max_length=250)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    position = models.CharField(max_length=250)
    company = models.CharField(max_length=250)
    website = models.CharField(max_length=250)
    linkedin = models.CharField(max_length=250)
    facebook = models.CharField(max_length=250)
    employees = models.CharField(max_length=250)
    stage = models.CharField(max_length=250)
    funding = models.CharField(max_length=250)
    video = models.CharField(max_length=250)
    idea = models.TextField()
    logo = models.CharField(max_length=250)
    presentation = models.CharField(max_length=250)
    date = models.DateTimeField()
    total_points = models.IntegerField(default=0)
    product_bar = models.IntegerField(default=0)
    team_bar = models.IntegerField(default=0)
    achievements_bar = models.IntegerField(default=0)
    market_bar = models.IntegerField(default=0)
    business_bar = models.IntegerField(default=0)
    presentation_bar = models.IntegerField(default=0)

class Stage(models.Model):
    stage1 = models.BooleanField(default=True)
    stage2 = models.BooleanField(default=False)




