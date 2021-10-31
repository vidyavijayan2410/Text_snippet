from django.contrib import admin

# Register your models here.

from .models import Text
from .models import Tag



class AdminText(admin.ModelAdmin):
    list_display = ['title', 'timestamp', 'user']


class AdminTag(admin.ModelAdmin):
    list_display = ['title']

# Register your models here.
admin.site.register(Text,AdminText)
admin.site.register(Tag,AdminTag)
