from django.contrib import admin
from crudmainapp.models import student

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display=('first_name','last_name','email','contact')
admin.site.register(student,StudentAdmin)