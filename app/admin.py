from django.contrib import admin
from .models import Category, Tag, Record

# Register your models here.

admin.site.register(Category)
admin.site.register(Tag)


@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'age', 'phone', 'category', 'created_at', 'updated_at']
    list_filter = ['category',]
    search_fields = ['first_name', 'last_name', 'phone']
    ordering= ['created_at']
    
    
admin.site.site_header = "CRM Adminstration"
admin.site.site_title = "CRM"
admin.site.index_title = "Welcome Back"