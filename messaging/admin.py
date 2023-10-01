# messaging/admin.py

from django.contrib import admin
from .models import Message

class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'timestamp')
    list_filter = ('sender', 'receiver', 'timestamp')
    search_fields = ('sender__username', 'receiver__username', 'content')
    date_hierarchy = 'timestamp'

admin.site.register(Message, MessageAdmin)
