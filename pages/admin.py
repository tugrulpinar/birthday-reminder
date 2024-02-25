from django.contrib import admin

from .models import BirthDayRecord


admin.site.register(BirthDayRecord)

admin_name = "Birthday Reminder Administration"
admin.site.site_title = admin_name
admin.site.site_header = admin_name