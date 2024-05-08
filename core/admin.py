from django.contrib import admin
from .models import *

class RecordAdmin(admin.ModelAdmin):
    list_display = ['created_at', 'full_name', 'biz_name', 'address', 'email', 'phone', 'category']

admin.site.register(Record, RecordAdmin)
