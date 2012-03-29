# -*- coding: UTF-8 -*-
from django.contrib import admin
from models import LoginAuditLog, UserProfile, Message

class LoginAuditLogAdmin(admin.ModelAdmin):
    pass

class UserProfileAdmin(admin.ModelAdmin):
    pass

class MessageAdmin(admin.ModelAdmin):
    pass

admin.site.register(LoginAuditLog, LoginAuditLogAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Message, MessageAdmin)
