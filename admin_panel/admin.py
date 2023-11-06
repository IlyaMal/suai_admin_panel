from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'first_name', 'last_name', 'group_number', 'ticket_number')

@admin.register(models.Query)
class QueryAdmin(admin.ModelAdmin):
    list_display = ('text', 'type', 'user')

@admin.register(models.WorkingDay)
class WorkingDayAdmin(admin.ModelAdmin):
    list_display = ('day_of_week', 'start_time', 'close_time', 'office')