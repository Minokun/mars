from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser

from help_tools.qiniuTool import getFileUrl

class UserProfile(AbstractUser):
    """
    用户
    """
    GENDER = {
        ('male', '男'),
        ('female', '女'),
        ('other', '你猜')
    }

    name = models.CharField(max_length=50, null=True, blank=True, verbose_name='昵称', help_text='昵称')
    avatar = models.ImageField(upload_to=getFileUrl, null=True, blank=True, verbose_name='头像', help_text='头像')
    email = models.CharField(max_length=100, null=True, blank=True, verbose_name='邮箱', help_text='邮箱')
    mobile = models.BigIntegerField( null=True, blank=True, verbose_name='电话', help_text='电话')
    gender = models.CharField(max_length=6, default='other', choices=GENDER, verbose_name='性别', help_text='性别')
    score = models.IntegerField(default=100, verbose_name='积分', help_text='积分')

    class Meta:
        verbose_name_plural = verbose_name = '用户信息'

    def __str__(self):
        return self.name


class VerifyPhoneCode(models.Model):
    '''
    电话验证码
    '''
    code = models.CharField(max_length=6, verbose_name='验证码', help_text='验证码')
    mobile = models.BigIntegerField(verbose_name='电话', help_text='电话')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间', help_text='添加时间')

    class Meta:
        verbose_name_plural = verbose_name = '短信验证码'

    def __str__(self):
        return self.code

class VerifyPicCode(models.Model):
    '''
    图片验证码
    '''
    code = models.CharField(max_length=10, verbose_name='图形验证码', help_text='图形验证码')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间', help_text='添加时间')

    class Meta:
        verbose_name_plural = verbose_name = '图片验证码'

    def __str__(self):
        return self.code