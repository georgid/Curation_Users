'''
Created on Jun 12, 2019

@author: joro
'''
from companies.views import create_user, login_company
from django.conf.urls import url

urlpatterns = [
    url('^create_user$', create_user, name='create_user'),
    url('^login_company$', login_company, name='login_company'),
    ]