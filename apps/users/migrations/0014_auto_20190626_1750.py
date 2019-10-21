# Generated by Django 2.1.4 on 2019-06-26 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_auto_20181217_2332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(choices=[('male', '男'), ('female', '女'), ('other', '你猜')], default='other', help_text='性别', max_length=6, verbose_name='性别'),
        ),
    ]