import json
import os

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from users.models import UserProfile

from rest_framework import status
from rest_framework import views
# Create your views here.

def test(request):
    """
    测试
    :param request:
    :return:
    """
    ret = UserProfile.objects.get(name='全世界').avatar.url
    return JsonResponse({'res': str(ret)}, status=status.HTTP_200_OK)