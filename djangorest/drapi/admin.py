from django.contrib import admin
from . models import Ai

# Register your models here.
@admin.register(Ai)
class AiAdmin(admin.ModelAdmin):
    list_display = ['id','tname','course_name','course_duration','seat']
