from django import template
from pages.models import *
from customuser.models import *

register = template.Library()



@register.filter
def get_rate_info(user_id, startup_id):
    stage = Stage.objects.get(id=1)
    if stage.stage1:
        rated = Rated.objects.filter(user_id=user_id)
    else:
        rated = RatedStage2.objects.filter(user_id=user_id)
    tt = []
    for i in rated:
        tt.append(i.startup.id)
    print(tt)
    print(startup_id)
    if startup_id in tt:
        return '<p class="color-green">Rate</p>'
    else:
        return '<p class="color-red">None</p>'

@register.filter
def get_rate_send(user_id, startup_id):
    stage = Stage.objects.get(id=1)
    if stage.stage1:
        rated = Rated.objects.filter(user_id=user_id)
    else:
        rated = RatedStage2.objects.filter(user_id=user_id)
    tt = []
    for i in rated:
        tt.append(i.startup.id)
    print(tt)
    print(startup_id)
    if startup_id in tt:
        return ' <span class="primary-btn">Arleady Rated</span>'
    else:
        return ' <a href="" class="primary-btn">Send notification</a>'

