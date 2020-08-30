from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import *
from django.contrib.auth.forms import UserCreationForm
from customuser.models import *
from django.core.mail import send_mail, send_mass_mail
from django.template.loader import render_to_string
import settings
from django.views.generic import View
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template

from xhtml2pdf import pisa

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None

class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        startups_data = StartUp.objects.all().order_by('-total_points')
        data = {
             'startups_data': startups_data,
        }
        pdf = render_to_pdf('pdf.html', data)
        return HttpResponse(pdf, content_type='application/pdf')
def index(request):
    form = UserCreationForm()
    if request.user.is_authenticated:


        localStartup = StartUp.objects.all().order_by('-total_points')
        all_rated = Rated.objects.filter(user=request.user)
        rated = []
        for i in all_rated:
            rated.append(i.startup.id)

    return render(request, 'index.html', locals())

def contests(request):

    return render(request, 'contests.html', locals())

def instructions(request):

    return render(request, 'instr.html', locals())

def startups(request,id):
    stage = Stage.objects.get(id=1)

    if stage.stage1:
        localStartup = StartUp.objects.all().order_by('-total_points')
        all_rated = Rated.objects.filter(user=request.user)
        rated = []
        for i in all_rated:
            rated.append(i.startup.id)
    else:
        temp = StartUp.objects.all().order_by('-total_points')[:settings.MAX_STAPTUPS_TOP_7]
        localStartup = []
        for i in temp:
            if i.contest == contest_cat:
                localStartup.append(i)


        all_rated = RatedStage2.objects.filter(user=request.user)
        rated = []
        for i in all_rated:
            rated.append(i.startup.id)
    return render(request, 'list.html', locals())

def admin(request,category_id):



    allStartups = Startups.objects.using('users').all()


    for startup in allStartups:
        if startup.approved == 'yes':
            temp, created = StartUp.objects.get_or_create(original_id=startup.id, defaults={
                'order':startup.order,
                'approved':startup.approved,
                'contest':startup.contest,
                'first_name':startup.first_name,
                'last_name':startup.last_name,
                'email':startup.email,
                'position':startup.position,
                'company':startup.company,
                'website':startup.website,
                'linkedin':startup.linkedin,
                'facebook':startup.facebook,
                'employees':startup.employees,
                'stage' :startup.stage,
                'funding':startup.funding,
                'video':startup.video,
                'idea' :startup.idea,
                'logo':startup.logo,
                'presentation':startup.presentation,
                'date':startup.date
            })
            if created:
                print('new record id', temp.id)
            else:
                print('record id exixts', temp.id)
        else:
            print('not appruved')


    localStartup = StartUp.objects.all().order_by('-total_points')

    listJury = User.objects.all()
    print(listJury)

    return render(request, 'admin.html', locals())

def invite(request):
    if request.POST:
        print(request.POST)
        user = User.objects.create(email=request.POST.get('email'),first_name=request.POST.get('name'), is_invited=True)

    allinvited = User.objects.filter(is_invited_person=True)

    return render(request, 'invite.html', locals())

def rate(request):
    print(request.POST)
    data=request.POST
    multiplier = 100
    startup = StartUp.objects.get(id=data.get('startup_id'))
    Rated.objects.create(startup=startup,
                         user=request.user)

    product_bar = int(data.get('product_bar').split('-')[1]) * multiplier
    team_bar = int(data.get('team_bar').split('-')[1]) * multiplier
    presentation_bar = int(data.get('presentation_bar').split('-')[1]) * multiplier
    market_bar = int(data.get('market_bar').split('-')[1]) * multiplier
    business_bar = int(data.get('business_bar').split('-')[1]) * multiplier

    startup.product_bar += product_bar
    startup.team_bar += team_bar
    startup.presentation_bar += presentation_bar
    startup.market_bar += market_bar
    startup.business_bar += business_bar

    startup.total_points += product_bar +\
                            team_bar +\
                            presentation_bar +\
                            market_bar +\
                            business_bar
    startup.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def rate_stage2(request):
    print(request.POST)
    data=request.POST
    multiplier = 100
    startup = StartUp.objects.get(id=data.get('startup_id'))
    RatedStage2.objects.create(startup=startup,
                         user=request.user)

    presentation_bar = int(data.get('presentation_bar').split('-')[1]) * multiplier


    startup.presentation_bar += presentation_bar


    startup.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def send_notify(request):
    print(request.GET)
    msg_html = render_to_string('not_rate_email.html', {'name':request.GET.get('name')})
    send_mail('Startup Evaluation Reminder', None, 'Pitch <pitch@inclusionforum.global>',
              [request.GET.get('email')],
              fail_silently=False, html_message=msg_html)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
def start_stage2(request):
    allStartups = StartUp.objects.all().order_by('-total_points')
    print(allStartups)
    top8 = allStartups[:settings.MAX_STAPTUPS_TOP_7]
    top20 = allStartups[settings.MAX_STAPTUPS_TOP_7:settings.MAX_STAPTUPS_TOP_20]
    other = allStartups[settings.MAX_STAPTUPS_TOP_20:]
    print(top8)
    print(top20)
    print(other)
    for i in top8:
        msg_html = render_to_string('top8_email.html', {'name':i.company})
        send_mail('Startup Pitch Contest Final', None, 'Pitch <pitch@inclusionforum.global>',
                  [i.email],
                  fail_silently=False, html_message=msg_html)
    for i in top20:
        msg_html = render_to_string('top20_email.html', {'name':i.company})
        send_mail('Startup Pitch Expo Qualified', None, 'Pitch <pitch@inclusionforum.global>',
                  [i.email],
                  fail_silently=False, html_message=msg_html)
    for i in other:
        msg_html = render_to_string('not_in_final_email.html', {'name':i.company})
        send_mail('Startup Pitch Contest Results', None, 'Pitch <pitch@inclusionforum.global>',
                  [i.email],
                  fail_silently=False, html_message=msg_html)

    stage = Stage.objects.get(id=1)
    stage.stage1 = False
    stage.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

