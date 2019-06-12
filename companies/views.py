from django.shortcuts import render
from rest_framework.decorators import api_view
from companies.serializer import UserSerializer
from rest_framework.response import Response
from rest_framework import status
from companies.models import Company, Permission, Permission_Role
from django.contrib.auth.models import User

errors = []
errors.append("You are not allowed. Please contact your company admin")
errors.append("You are not allowed. Please contact system admin")
errors.append("You company reached max. user limit. please contact with us and upgrade your plan")



        

# Create your views here.
@api_view(['POST'])
def create_user(request):
    """
    create new user
    """

    if request.method == 'POST':
        
        # get current user
#         curr_user = request.user
        curr_user = User.objects.get(pk=2)
        company_id = 1
        curr_company =  Company.objects.get(pk=1) 
        
        #@## block using role system
        p1 = Permission.objects.filter(name='Create User')[0]
        
        error_id = Permission_Role.get_error_for_permission(user=curr_user, company=curr_company, permission=p1)
        if error_id:
            return Response(errors[error_id-1], status=status.HTTP_400_BAD_REQUEST)
        
        ##### block using license system
        error_id = 3
        if curr_company.get_num_users() == curr_company.get_allowed_users():
            return Response(errors[error_id-1], status=status.HTTP_400_BAD_REQUEST)
        
        #### store user
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)