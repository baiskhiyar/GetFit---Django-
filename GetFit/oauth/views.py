from django.http import HttpResponse 
from django.shortcuts import render 
from oauth.http_views.create_user import CreateUserView
from oauth.http_views.get_user import GetUser

# Create your views here.


def health_check(request) : 
    return HttpResponse("WORKING") ; 
