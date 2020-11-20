from django.contrib import admin
from core.models import event

# Register your models here.

class EventAdmin(admin.ModelAdmin):
    list_display = ('id','title','data_event','data_create')
    list_filter = ('user', 'data_event',)

admin.site.register(event, EventAdmin)