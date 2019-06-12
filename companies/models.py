from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class License(models.Model):
    name = models.CharField(max_length=50)
    num_users_allowed = models.IntegerField()
    
    
class Company(models.Model):
    name = models.CharField(max_length=50)
    
    license = models.ForeignKey(
        License,
        blank=True,
        null=True,
#         related_name='licence',
        on_delete=models.CASCADE
    )
    
    def get_allowed_users(self):
        '''
        which license is associated
        &
        how many users allowsed according to it
        '''
        return self.license.num_users_allowed
    
    def get_num_users(self):
        
        return User_Company_Role.get_num_users(self.pk)
    
        
    
class Role(models.Model):
    name =  models.CharField(max_length=50)   

class User_Company_Role(models.Model):
    
    user = models.ForeignKey(
        User,
        blank=True,
        null=True,
        related_name='user',
        on_delete=models.CASCADE
    )
    company = models.ForeignKey(
        Company,
        blank=True,
        null=True,
        related_name='company',
        on_delete=models.CASCADE
    )
    
    role = models.ForeignKey(
        Role,
        blank=True,
        null=True,
        related_name='role',
        on_delete=models.CASCADE
    )
    @staticmethod
    def get_role(user, company):
        '''
        Reutrn the role for a user with user_id logged in company with company_id
        '''
        
        q1 = User_Company_Role.objects.filter(user = user)
        role_rel = q1.filter(company = company )
        r = role_rel[0].role
        return r 
    
    @staticmethod
    def get_num_users(company_id):
        '''
        retuns the number of users for a given comapany with
        :param: 
        '''
        c = Company.objects.get(pk=company_id)
        users = User_Company_Role.objects.filter(company=c)
        return len(users) 
    
class Permission(models.Model):
    name =   models.CharField(max_length=50)
    code =   models.IntegerField()
    # 1 meeans boeolean, 2 means numeric
    Type = models.IntegerField()  
    
    
    
class  Permission_Role(models.Model):
        
        permission = models.ForeignKey(
        Permission,
        blank=True,
        null=True,
        related_name='permission',
        on_delete=models.CASCADE
    )
        
        role = models.ForeignKey(
        Role,
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )
        # store only the error
        error_id = models.IntegerField()
        
        @staticmethod
        def get_error_for_permission( user, company, permission):
            '''
            Get the role for this user witin the company company
            Then for the given parmission, return an error. 
            If it returns None, then the user is allowed to execute the pemission 
            '''
            role = User_Company_Role.get_role(user, company)
            
            q1 = Permission_Role.objects.filter(role = role)
            q2 = q1.filter(permission = permission)
            if q2:
                return q2[0].error_id
            else:
                return None
            
    
#     models.CharField(max_length=50)