from rest_framework.views import APIView 
from django.http import JsonResponse
from django.core import serializers


from oauth.models import User

class GetUser(APIView) : 

    def get(self , request) : 
        users = list(User.objects.filter(active=1))
        response = serializers.serialize('json' , users)
        return JsonResponse({'data': response}) 