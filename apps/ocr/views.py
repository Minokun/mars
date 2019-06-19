from django.shortcuts import render
from .serializer import PicTextCommonListSerializer
from .models import PicTextCommon
from rest_framework.authentication import SessionAuthentication, BaseAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.
from rest_framework import mixins, viewsets

class PicList(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    """
    图文识别列表
    list:
        获取列表
    create:
        创建识别
    delete:
        删除

    """
    serializer_class = PicTextCommonListSerializer
    queryset = PicTextCommon.objects.all()
    authentication_classes = (SessionAuthentication, BaseAuthentication)
    permission_classes = (IsAuthenticated, )