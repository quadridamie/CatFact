'''
Created on Sep 20, 2016

@author: Damilola
'''
from django.conf.urls import url
from . import views


urlpatterns =[
              
             url(r'^home/$', views.home, name='home_page'),
             url(r'^namedcat/$', views.namedCat, name='named_cat_page'),
             url(r'^addname/$', views.addName, name='add_name_page'),
              
              
]