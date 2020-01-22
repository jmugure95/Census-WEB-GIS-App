from django.contrib import admin
from django.conf.urls import url,include
from censuskenya.views import *
from rest_framework import routers

# router = routers.DefaultRouter()


urlpatterns = [
 	url(r'^$', Home, name='home'),
 	url(r'^graphs/',Graphs,name='graphs'),
 	url(r'^population/',population,name='population'),
 	url(r'^watuka/',watuka,name='watuka'),
 	url(r'^spouse/',Spous,name='spous'),
 	url(r'^head/',Heady,name='head'),
 	url(r'^head_api/',Headserial.as_view(),name='head_api'),
 	url(r'^spouse_api/',Spouseserial.as_view(),name='spouse_api'),
 	url(r'^child_api/',Childserial.as_view(),name='child_api'),
 	url(r'^watuka_api/',Watukaserial.as_view(),name='watuka_api'),
 	url(r'^analy/',AnalyticalView,name='analy'),
   
]
