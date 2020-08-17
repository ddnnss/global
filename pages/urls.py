from django.urls import path,include
from . import views

urlpatterns = [


    path('', views.index, name='index'),
    path('contests', views.contests, name='contests'),
    path('startups/<id>', views.startups, name='startups'),
    path('admin_page/jury/invite', views.invite, name='invite'),
    path('admin_page/<category_id>', views.admin, name='admin_page'),

    path('rate', views.rate, name='rate'),
    path('rate_stage2', views.rate_stage2, name='rate_stage2'),
    path('start_stage2', views.start_stage2, name='start_stage2'),

]
