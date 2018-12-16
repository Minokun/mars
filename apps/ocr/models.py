from datetime import datetime

from django.db import models

from help_tools.qiniuTool import getFileUrl
# Create your models here.

class PicTextCommon(models.Model):
    class Meta:
        verbose_name = "Ocr通用文字识别"
        verbose_name_plural = verbose_name

    pic_file = models.ImageField(upload_to=getFileUrl, verbose_name='图片链接地址', help_text='图片链接地址')
    res_text = models.TextField(null=True, blank=True, verbose_name='识别出的文字', help_text='识别出的文字')
    words_result_num = models.IntegerField(default=0, verbose_name='文本行数', help_text='文本行数')
    language_type = models.CharField(max_length=20, default='')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间', help_text='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间', help_text='更新时间')