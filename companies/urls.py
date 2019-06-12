'''
Created on Jun 12, 2019

@author: joro
'''
from companies.views import create_user
from django.conf.urls import url

urlpatterns = [
    url('^create_user$', create_user, name='create_user'),
    ]