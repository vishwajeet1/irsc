from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from .models import Users
from .utils import passValid, emailValid, hashfun
import json
# Create your views here.
@api_view(['POST'])
@csrf_exempt
def sign(request):
    '''
    param:
    {
        "username":"newid1",
        "password":"Password@123",
        "fname":"ram",
        "lname":"lakhan",
        "email":"vishwajeetrai1996@gmail.com",
        "phone":"9873113386"
        }
    '''
    try:
        try:
            req = request.data['_content']
            data = json.loads(req)
        except:
            data = request.data

        username = data['username']
        password = data['password']
        fname = data['fname']
        lname = data['lname']
        email = data['email']
        phone = data['phone']
        try:
            user = Users.objects.get(username=username)
            return JsonResponse(
                {
                    "status": False,
                    "error": "user already exists"
                }, status=status.HTTP_409_CONFLICT)
        except Users.DoesNotExist:
            if passValid(password):
                return JsonResponse(
                    {
                        "status": False,
                        "error": passValid(password)
                    }, status=status.HTTP_409_CONFLICT)
            if emailValid(email) == False:
                return JsonResponse(
                    {
                        "status": False,
                        "error": "email not valid"
                    }, status=status.HTTP_409_CONFLICT)

            password = hashfun(password)
            user = Users.objects.create(
                username=username, password=password, fname=fname, lname=lname, email=email, phone=phone)
            user.save()
            return JsonResponse(
                {
                    "status": True,
                    "data": {
                        "user_data": {
                            "username": user.username,
                            "first_name": user.fname,
                            "last_name": user.lname,
                            "email": user.email,
                            "phone": user.phone
                        }
                    }
                }, status=status.HTTP_200_OK)
    except Exception as e:
        s = "Error {0}".format(str(e))  # string
        msg = s.encode("utf-8")
        return JsonResponse(
            {
                "status": False,
                "errorCode": status.HTTP_400_BAD_REQUEST,
                "message": msg,
                "data": {
                }
            }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@csrf_exempt
def login(request):
    '''
    param:
    {
        "username":"newid1",
        "password":"Password@123"
    }
    '''
    try:
        try:
            req = request.data['_content']
            data = json.loads(req)
        except:
            data = request.data

        username = data['username']
        password = data['password']

        try:
            user = Users.objects.get(username=username)
            password = hashfun(password)
            if user.password == password:
                return JsonResponse(
                    {
                        "status": True,
                        "data": {
                            "user_data": {
                                "username": user.username,
                                "first_name": user.fname,
                                "last_name": user.lname,
                                "email": user.email,
                                "phone": user.phone
                            }
                        }
                    }, status=status.HTTP_200_OK)

            else:
                return JsonResponse(
                    {
                        "status": False,
                        "error": "password incorrect"
                    }, status=status.HTTP_409_CONFLICT)

        except Users.DoesNotExist:
            return JsonResponse(
                {
                    "status": False,
                    "error": "user does not exist"
                }, status=status.HTTP_409_CONFLICT)

    except Exception as e:
        s = "Error {0}".format(str(e))  # string
        msg = s.encode("utf-8")
        return JsonResponse(
            {
                "status": False,
                "errorCode": status.HTTP_400_BAD_REQUEST,
                "message": msg,
                "data": {
                }
            }, status=status.HTTP_400_BAD_REQUEST)
