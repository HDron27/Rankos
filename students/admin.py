from django.contrib import admin
from .models import Student, Group, Club

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ['name', 'curator']

@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'age', 'group']
    filter_horizontal = ['clubs']
