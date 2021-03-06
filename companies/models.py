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
        how many users allowed according to the license associated to the company
        '''
        return self.license.num_users_allowed
    
    def get_num_users(self):
        '''
        get the number users working in this company
        '''
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
        retuns the number of users for a given company
        :param: company_id
        '''
        c = Company.objects.get(pk=company_id)
        users = User_Company_Role.objects.filter(company=c)
        return len(users) 
    
class Permission(models.Model):
    name =   models.CharField(max_length=50)
    code =   models.IntegerField()
    # 1 meeans boeolean, 2 means numeric
    Type = models.IntegerField() 
    
    def get_role_error(self, role):
        '''
        if with the given role the permission is allowed. Returns error if not allowed. 
        Returns empty object otherwise
        
        :param role - the given role
        :return - returns the error 
        '''
        q1 = Permission_Role.objects.filter(role = role)
        q2 = q1.filter(permission = self) 
        return q2   
    
    
    
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
            not_allowed = permission.get_role_error(role)

            if not_allowed:
                return not_allowed[0].error_id
            else:
                return None
            
