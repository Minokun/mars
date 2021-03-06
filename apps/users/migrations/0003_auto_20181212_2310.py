# Generated by Django 2.1.4 on 2018-12-12 15:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20181212_2305'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime.now, help_text='创建时间', verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(choices=[('female', '女'), ('male', '男'), ('other', '你猜')], help_text='性别', max_length=6, verbose_name='性别'),
        ),
    ]
