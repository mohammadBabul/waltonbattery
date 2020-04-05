from django.contrib import admin
from battery.models import BatteryDataSet
from battery.models import Category
from battery.models import Result

from django.contrib.admin.models import LogEntry
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

admin.site.site_header = "Battery Log"
admin.site.site_title  = "Battery Log DashBoard"

LogEntry.objects.all().delete()


class PhoneModelAdmin(admin.ModelAdmin):
    site_header = "Nothing"
    list_display = ('serial_no','time', 'charging_level','temperature', 'battery_voltage','decreased_voltage',
    'charging_status' )
   # search_fields =('ime_numner',)
    list_filter = ('serial_no',)


class ResultAdmin(admin.ModelAdmin):
    site_header = "Nothing"
    list_display = ('imei','result', 'model')
    list_filter =  ('imei','result', 'model')
    search_fields =('imei',)
     

admin.site.register(BatteryDataSet, PhoneModelAdmin)
admin.site.register(Result, ResultAdmin)
admin.site.register(Category)
admin.site.unregister(Group)
admin.site.unregister(User)
