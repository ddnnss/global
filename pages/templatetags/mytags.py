from django import template
from pages.models import *
from customuser.models import *

register = template.Library()



@register.filter
def get_rate_info(user_id, startup_id):
    rated = Rated.objects.filter(user_id=user_id)
    tt = []
    for i in rated:
        tt.append(i.startup.id)
    # print(tt)
    # print(startup_id)
    if startup_id in tt:
        return '<p class="color-green">Rate</p>'
    else:
        return '<p class="color-red">None</p>'

@register.filter
def get_rate_send(user_id, startup_id):


    user = User.objects.get(id=user_id)

    rated = Rated.objects.filter(user_id=user_id)

    tt = []
    for i in rated:
        tt.append(i.startup.id)
    # print(tt)
    # print(startup_id)
    if startup_id in tt:
        return ' <span class="primary-btn">Arleady Rated</span>'
    else:
        return f' <a href="/send_notify?email={user.email}" class="primary-btn">Send notification</a>'

@register.filter
def get_rate_status(startup_id):
    print(startup_id)
    startup= StartUp.objects.get(id=startup_id)
    print(startup)
    rated_count = 0
    listJury = User.objects.all()
    print(listJury)
    rated_users = []
    rate = Rated.objects.filter(startup_id=startup_id)
    for r in rate:
        rated_users.append(r.user)
    for user in listJury:
        if user in rated_users:
            rated_count +=1
    print('rated_count',rated_count)
    if rated_count == len(listJury):
        return '<div class="startup-rated">All rate</div>'
    else:
        return '<div class="startup-rated notActive">Did not rate</div>'
