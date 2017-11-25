from django.contrib import admin
from app.models import Record

class RecordAdmin(admin.ModelAdmin):
    list_display = ('user','teacher_name','grade', 'timestamp',)
    search_fields = ['user', 'teacher_name']
    list_filter = ('user','teacher_name','grade',)

admin.site.register(Record, RecordAdmin)
