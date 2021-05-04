from rest_framework.decorators import api_view
from rest_framework import serializers
from rest_framework.response import Response


from .serializer import *
from rest_framework.authtoken.models import Token



@api_view(['POST'])
def registration_api(request):

    serializer = registrationSerializer(data=request.data)

    if serializer.is_valid():
        user = serializer.save()
        token = Token.objects.get(user=user).key
        context = {
            'response' : 'successfully created account',
            'email' : user.email,
            'username' : user.email,
            'token' : token
        }

    else:
        context = {
            'errors' : serializer.errors
        }
    return Response(context)

