from django.urls import path
from . import views

urlpatterns = [
   path('logout/', views.logout_page, name='logout_page'),
   path('signup/', views.signup, name='signup'),


]
