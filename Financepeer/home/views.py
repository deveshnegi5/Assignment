import json
from logging import exception
from multiprocessing import context
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from .models import UserInfo
from .serializers import UserInfoSerializer
from django.shortcuts import render
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
from rest_framework.authentication import SessionAuthentication,  BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from home import serializers

class Userview(APIView):
    auth_class = [SessionAuthentication,BasicAuthentication,TokenAuthentication]
    permission_class = [IsAuthenticated]
    def get(self,request,format=None):
        content={
            'user' :str(request.user),
            'auth': str(request.auth),

        }
        return Response(content)

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,context={'request':request})
        serializer.is_valid(raise_exception = True)
        user = serializer.validated_data['user']
        token,created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'username': user.username,
            'first_name': user.first_name,
            'last_name':user.last_name,
            'user_id':user.pk,
            'email':user.email
        }

        )

@csrf_exempt
def home(request):
    if request.method == 'GET':
        user = UserInfo.objects.all()
        user_serializer = UserInfoSerializer(user, many=True)
        return JsonResponse(user_serializer.data, safe=False)

    elif request.method == 'POST':
        try:
            ROOT_FILE = settings.MEDIA_ROOT + '\FinancePeer_Assignment_Data.json'
            with open(ROOT_FILE, 'r') as data:
                parsed_json = json.load(data)

            for result in parsed_json:
                UserInfo.objects.create(
                userId = result['userId'],
                id = result['id'],
                title=result['title'],
                body = result['body'], 
            ) 
            user_data = JSONParser().parse(request)
            user_serializer = UserInfoSerializer(data=user_data)
            if user_serializer.is_valid():
                user_serializer.save()
                return JsonResponse('Record is posted', safe=False)
            return JsonResponse('Record not posted.', safe=False)

        except Exception as e:
            print(e)

@csrf_exempt
def SaveFile(request):
    try:
        file=request.FILES
        val = file['uploadedFile']
        file_name = default_storage.save(val.name,val)

        return JsonResponse(file_name,safe=False)
    except Exception as e:
            print(e)