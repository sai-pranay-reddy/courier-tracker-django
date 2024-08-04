from django.contrib import admin
from .models import Courier


class CourierAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'student_rollno', 'date_recieved', 'service','center')
	change_list_template = 'admin/change_list.html'
	actions = None

admin.site.site_header = 'CMS Administration'
admin.site.site_title = 'CMS-Admin'
admin.site.register(Courier, CourierAdmin)