# Generated by Django 2.1.4 on 2018-12-16 16:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PicTextCommon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic_url', models.URLField(help_text='图片链接地址', verbose_name='图片链接地址')),
                ('res_text', models.TextField(blank=True, help_text='识别出的文字', null=True, verbose_name='识别出的文字')),
                ('words_result_num', models.IntegerField(help_text='文本行数', verbose_name='文本行数')),
                ('language_type', models.CharField(default='', max_length=20)),
                ('create_time', models.DateTimeField(default=datetime.datetime.now, help_text='创建时间', verbose_name='创建时间')),
            ],
            options={
                'verbose_name': 'Ocr通用文字识别',
                'verbose_name_plural': 'Ocr通用文字识别',
            },
        ),
    ]
