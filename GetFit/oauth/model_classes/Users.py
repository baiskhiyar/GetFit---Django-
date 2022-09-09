from django.db import models 
from django.http import HttpResponse
from rest_framework.views import APIView 
from rest_framework.response import Response


class User(models.Model) : 
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    username = models.CharField(max_length=30)
    mobile_no = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    city = models.CharField(max_length=100)
    age = models.IntegerField() ; 
    password = models.CharField(max_length=30) 
    active = models.IntegerField(default=1)
    
    class Meta : 
        db_table = 'users' 
        managed = True 



    def get(request) : 
        response = User.objects.filter(active=1) ; 
        return Response(response)


