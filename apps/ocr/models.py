from datetime import datetime

from django.db import models
from django.dispatch import receiver
from django.db.models import signals

from help_tools.qiniuTool import getFileUrl
from help_tools.baidu_api import BDApi, LANGUAGE_TYPE
# Create your models here.

class PicTextCommon(models.Model):
    class Meta:
        verbose_name = "Ocr通用文字识别"
        verbose_name_plural = verbose_name

    pic_file = models.ImageField(upload_to=getFileUrl, verbose_name='图片链接地址', help_text='图片链接地址')
    res_text = models.TextField(null=True, blank=True, verbose_name='识别出的文字', help_text='识别出的文字')
    words_result_num = models.IntegerField(default=0, verbose_name='文本行数', help_text='文本行数')
    language_type = models.CharField(choices=LANGUAGE_TYPE, max_length=20, verbose_name='语言选择', help_text='语言选择')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间', help_text='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间', help_text='更新时间')


@receiver(signal=signals.post_save, sender=PicTextCommon)
def ocrRecOp(instance, created, **kwargs):
    if created:
        # 对上传的图片进行识别
        url = instance.pic_file.url
        # 通过百度Api识别图片文字
        bd = BDApi()
        res = bd.common_text_recognize(url, 1, language_type=instance.language_type)
        if 'error_msg' in res.keys():
            print('七牛云图片上传错误！')
        else:
            instance.words_result_num = res['words_result_num']
            instance.res_text = ''.join([i['words'] + '\r\n' for i in res['words_result']])
            instance.save()