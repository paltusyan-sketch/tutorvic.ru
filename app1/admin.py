from django.contrib import admin
from .models import Subjects, Settings

# Register your models here.

admin.site.register(Subjects)

@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    pass

