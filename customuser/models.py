from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.db.models.signals import post_save
from django.core.mail import send_mail
from django.template.loader import render_to_string
import datetime as dt
from .utils import *
from datetime import datetime
from django.utils import timezone
from pages.models import *
import uuid
class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

class Category(models.Model):
    name=models.CharField('Category',max_length=255,blank=False,null=True)

    def __str__(self):
        return f'{self.id} | {self.name}'

class User(AbstractUser):
    username = None
    category = models.ManyToManyField(Category,blank=False,null=True,verbose_name='User categories')
    avatar = models.ImageField('Avatar', upload_to='user',blank=True,null=True)
    first_name = models.CharField('First name', max_length=50, blank=True, null=True)
    last_name = models.CharField('Last name', max_length=50, blank=True, null=True)
    email = models.EmailField('e-mail', blank=True, null=True, unique=True)
    temp_password = models.CharField('temp_password',max_length=255, blank=True, null=True)
    is_invited = models.BooleanField('Invited ?', default=False)
    is_invited_person = models.BooleanField('Invited Person?', default=False)

    is_active = models.BooleanField('Active User', default=True)
    verify_code = models.CharField('verify_code', max_length=255, blank=True, null=True)
    technique_added = models.IntegerField(default=0)
    rate_times = models.IntegerField(default=0)
    other_added = models.IntegerField(default=0)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def save(self, *args, **kwargs):
        if self.is_invited:
            self.temp_password = create_random_string(num=8)
            self.set_password(self.temp_password)

        super(User, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.id} | {self.email} | Active : {self.is_active}'


    def get_full_name(self):
        if self.last_name:
            return f'{self.last_name} {self.first_name}'
        else:
            return f'{self.first_name}'

    def get_avatar(self):
        if self.avatar:
            return self.avatar.url
        else:
            return '/static/img/user.png'



def user_post_save(sender, instance, created, **kwargs):

    if created:
        if instance.is_invited:
            msg_html = render_to_string('invite_email.html', {
                                                              'name': instance.first_name,
                                                              'email': instance.email,
                                                              'password': instance.temp_password
                                                              })
            send_mail('Startup Evaluation Platform Invite', None, 'tickets@inclusionforum.global',
                      [instance.email],
                      fail_silently=False, html_message=msg_html)
            instance.is_active = False
            instance.is_invited_person = True
            instance.save()


post_save.connect(user_post_save, sender=User)


class Rated(models.Model):
    startup =  models.ForeignKey(StartUp,blank=True,on_delete=models.CASCADE,null=True)
    user = models.ForeignKey(User,blank=True,on_delete=models.CASCADE,null=True)

class RatedStage2(models.Model):
    startup =  models.ForeignKey(StartUp,blank=True,on_delete=models.CASCADE,null=True)
    user = models.ForeignKey(User,blank=True,on_delete=models.CASCADE,null=True)

