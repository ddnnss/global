from django.contrib.auth import  logout,login, authenticate
from customuser.models import *
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
import uuid

import datetime as dt
from datetime import datetime
from django.utils import timezone

def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')



def signup(request):
    if request.method == 'POST':
        user = None
        try:
            temp_user = User.objects.get(email=request.POST.get('email'))
            print(temp_user)
            if temp_user.is_invited and not temp_user.is_active:
                temp_user.is_active = True
                temp_user.is_invited = False
                temp_user.save()
            temp_user = User.objects.get(email=request.POST.get('email'))
            user = authenticate(username=temp_user.email, password=request.POST.get('password'))
        except:
            pass
        if user:
            login(request, user)
        else:
            print('user not found')
        return HttpResponseRedirect('/')
    else:
        form = UserCreationForm()
        return HttpResponseRedirect('/')




