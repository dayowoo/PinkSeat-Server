from django.contrib import admin
from import_export.admin import ExportActionModelAdmin, ImportExportMixin, ImportMixin

from PinkSeat_seat.models import Subway, SubSchedule, Seat_info, Reservation


class ScheduleAdmin(ImportExportMixin, admin.ModelAdmin):
    pass


# Register your models here.
admin.site.register(Seat_info)
admin.site.register(Reservation)
admin.site.register(Subway)
admin.site.register(SubSchedule, ScheduleAdmin)