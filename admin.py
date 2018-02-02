from django.contrib import admin
from blog.models import *


class BlogAdmin(admin.ModelAdmin):
    list_display = ['id','title','category','date_time','update_time']
# Register your models here.
admin.site.register(Blog,BlogAdmin)