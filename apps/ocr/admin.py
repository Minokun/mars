from django.utils.safestring import mark_safe
from django.contrib import admin

# Register your models here.
from ocr.models import *

class PicTextCommonAdmin(admin.ModelAdmin):
    def upload_img(self, obj):
        try:
            img = mark_safe('<img src="%s" width="50px" />' % (obj.pic_file.url,))
        except Exception as e:
            img = ''
        return img

    upload_img.short_description = 'Thumb'
    upload_img.allow_tags = True
    list_display = ['upload_img', 'language_type', 'words_result_num', 'res_text', 'create_time', 'update_time']
    readonly_fields = ['upload_img']

admin.site.register(PicTextCommon, PicTextCommonAdmin)