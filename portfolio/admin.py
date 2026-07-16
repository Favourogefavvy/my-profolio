from django.contrib import admin
from .models import Skill, Contact

# Register your models here.
@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'level', 'description', 'image')
    search_fields = ('name', 'level')
    
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'message', 'created_at')
    search_fields = ('name', 'email', 'subject')