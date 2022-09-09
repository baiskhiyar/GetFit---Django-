from rest_framework.views import APIView 
from django.http import HttpResponse 
from django.db import transaction 
from oauth.model_classes.Users import User

class CreateUserView(APIView) :
    
    @staticmethod 
    def create_user(request) : 

        data = request.data 
        print(data)

        first_password = data.get('firstpassword') 
        second_password = data.get('secondpassword') 

        if first_password != second_password : 
            return HttpResponse("Both the passwords should be same")
        
        email = data.get('email')
        existing_email = User.objects.filter(email=email).first() 
        if existing_email : 
            return HttpResponse("Email already exits!")
        
        username = data.get('username')
        existing_username = User.objects.filter(username=username).first() ; 
        if existing_username : 
            return HttpResponse("Username already exists!")
        
        new_user = User() 
        new_user.firstname = data.get('firstname')
        new_user.lastname = data.get('lastname') 
        new_user.username = username 
        new_user.mobile_no = data.get('mobile_no')
        new_user.email = email 
        new_user.city = data.get('city') 
        new_user.age = data.get('age')
        new_user.password = data.get('first_password') 
        new_user.save() 

        return HttpResponse("User has been created successfully") 

    
    @transaction.atomic 
    def post(self , request) : 
        response = self.create_user(request) 
        return response
        