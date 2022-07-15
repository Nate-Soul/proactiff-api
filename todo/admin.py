from django.contrib import admin
from .models import Todo

# Register your models here.
class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'day', 'reminder')
    
admin.site.register(Todo, TodoAdmin)