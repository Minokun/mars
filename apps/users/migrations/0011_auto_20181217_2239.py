# Generated by Django 2.1.4 on 2018-12-17 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20181217_0031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(choices=[('female', '女'), ('other', '你猜'), ('male', '男')], default='other', help_text='性别', max_length=6, verbose_name='性别'),
        ),
    ]
