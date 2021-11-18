from django.contrib import admin
from import_export.admin import ExportActionModelAdmin, ImportExportMixin, ImportMixin

from .models import SubSchedule


# Register your models here.
class SubScheduleAdmin(ImportExportMixin, admin.ModelAdmin):
    pass


admin.site.register(SubSchedule, SubScheduleAdmin)