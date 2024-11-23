from django.contrib import admin
from Ecomapp .models import Setting
# Register your models here.

class SettingAdmin(admin.ModelAdmin):
    list_display = ['id','title','email','status','contact','status','created_at','updated_at']

admin.site.register(Setting, SettingAdmin)