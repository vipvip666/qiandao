from django.contrib import admin

# Register your models here.
from .models import student_sign_in

class St_sinManager(admin.ModelAdmin):
    list_display = ['id', 'name', 'sign_time']
    list_display_links = ['name']
    search_fields = ['name']



admin.site.register(student_sign_in,St_sinManager)