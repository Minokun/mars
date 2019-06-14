from rest_framework import serializers
from .models import *


class PicTextCommonListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PicTextCommon
        exclude = ['id']