from django.contrib import admin
from django.utils.safestring import mark_safe

from users.models import *

# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
    def upload_img(self, obj):
        try:
            img = mark_safe('<img src="%s" width="50px" />' % (obj.avatar.url,))
        except Exception as e:
            img = ''
        return img

    upload_img.short_description = 'Thumb'
    upload_img.allow_tags = True
    list_display = ('name', 'mobile', 'gender', 'score', 'upload_img')
    readonly_fields = ['upload_img']
    search_fields = ('name', 'email')



admin.site.register(UserProfile, UserProfileAdmin)