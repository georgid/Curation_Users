'''
Created on Jun 12, 2019

@author: joro
'''
from rest_framework import serializers
from .models import Company
from django.contrib.auth.models import User


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ("name")
        
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'