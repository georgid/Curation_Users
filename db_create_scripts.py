# export DJANGO_SETTINGS_MODULE=curation.settings

import django
django.setup()

from companies.models import Permission
from companies.models import Role
from companies.models import Permission_Role
from companies.models import Company
from companies.models import User_Company_Role
from django.contrib.auth.models import User


# License: 
l1 = License(name='Free Plan', num_users_allowed=1)

l1 = License(name='Basic License Plan', num_users_allowed=3)

l2 = License(name='Basic License Plan', num_users_allowed=3)

l1 = License(name='Free Plan', num_users_allowed=1)

l3 = License(name='Professional License Plan', num_users_allowed=5)

l1.save()

l2.save()

l3.save()


# Roles


from companies.models import Role

r1 = Role(name='Ordinary User')

r2 = Role(name='Company Admin')

r3 = Role(name='System Admin')

r1.save()

r2.save()

r3.save()


# Users
u1 = User (username='A', password ='password')
u1.save()


# Companies
c1 = Company.objects.get(pk=1)
l2 = License.objects.get(pk=2)
c1.license = l2
c1.save()


# Relationships
ucr1 = User_Company_Role(user=u1, company=c1, role=r2)
In [33]: ucr2 = User_Company_Role(user=a[1], company=c[1], role=r1)

In [34]: ucr2.save()


# Permisssion

p1 = Permission(name='Create User', code = 1, Type = 1)
p.save()

Permission(name='Delete User', code = 2, Type=1)
p2.save()

Permission(name='Create Orgnisation', code = 3, Type=1)
p3.save()


# Permission Role Map

r1 = Role.objects.filter(name='Ordinary User')
r1= r1[0]

r2 = Role.objects.filter(name='Company Admin')
r2= r2[0]

pr1 = Permission_Role(permission=p1,role=r1,error_id =1 )
pr1.save()


pr2 = Permission_Role(permission=p2,role=r1,error_id =1 )
pr2.save()

pr3 = Permission_Role(permission=p3,role=r1,error_id =2 )
pr3.save()

pr4 = Permission_Role(permission=p3,role=r2,error_id =2 )
pr4.save()


