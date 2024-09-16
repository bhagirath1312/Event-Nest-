from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'time', 'location')
    search_fields = ('title', 'location')