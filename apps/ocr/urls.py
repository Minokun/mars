from django.conf.urls import url, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

# 文档识别
router.register(r'pic_rec', PicList, base_name='pic_rec')

urlpatterns = [
    url(r'', include(router.urls))
]