from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'group_number', 'ticket_number', 'telegram_id')

@admin.register(models.Query)
class QueryAdmin(admin.ModelAdmin):
    list_display = ('text', 'type', 'user')