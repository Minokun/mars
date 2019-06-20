import json
import os

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from users.models import UserProfile

from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework import views
# Create your views here.

def test(request):
    """
    测试
    :param request:
    :return:
    """
    for user in UserProfile.objects.all():
        Token.objects.get_or_create(user=user)
    return JsonResponse({'res': 'ok'}, status=status.HTTP_200_OK)