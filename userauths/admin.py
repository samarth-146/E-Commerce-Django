from django.contrib import admin

from .models import User

class ClassAdmin(admin.ModelAdmin):
    list_display=['username','email']
    
admin.site.register(User,ClassAdmin)
# Register your models here.
