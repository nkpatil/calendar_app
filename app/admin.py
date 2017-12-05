from django.contrib import admin
from app.models import Record

class RecordAdmin(admin.ModelAdmin):
    list_display = ('user','teacher_name','grade', 'timestamp', 'district')
    search_fields = ['user', 'teacher_name', 'district']
    list_filter = ('user','teacher_name','grade', 'district')

admin.site.register(Record, RecordAdmin)
