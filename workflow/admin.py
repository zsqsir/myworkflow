
from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin
class NoticesAdmin(SummernoteModelAdmin):
    list_display = ['title','updated','created']
    list_filter = ( 'title', 'content')
    search_fields = ('title', 'content')
    date_hierarchy = 'updated'
    ordering = ['-updated',]
admin.site.register(Notices,NoticesAdmin)

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['person_name','department_name','level']
    list_filter = ('person__first_name', 'department_name','level')
    search_fields = ('person__first_name','department_name','level')
    ordering = [ 'department_name', ]
    raw_id_fields = ('person',)
admin.site.register(Department,DepartmentAdmin)

class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['applicant_name','department','reason']
    list_filter = ('applicant__first_name', 'department')
    search_fields = ('applicant__first_name','department')
    ordering = [ 'department', ]
    fields = ('applicant',('start_date','finished_date'),'reason','status','reply','department')
    # raw_id_fields = ('applicant',)
admin.site.register(Leave_application,ApplicationAdmin)
class Reimbursement_personAdmin(admin.ModelAdmin):
    list_display = ['reimbursement_of_person','money']
    list_filter = ('reimbursement_person__first_name', 'department')
    search_fields = ('reimbursement_person__first_name', 'department')
    ordering = ['department', ]
admin.site.register(reimbursement, Reimbursement_personAdmin)

class WorksheetAdmin(admin.ModelAdmin):
    list_display = ['worksheet_person','title','who_is_processing','create_time']
    list_filter =['creater__first_name']
admin.site.register(worksheet,WorksheetAdmin)
