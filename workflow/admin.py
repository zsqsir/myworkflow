
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

class UpFileAdmin(admin.ModelAdmin):
    list_display = ['upfile_of_person','title','detail']#,'file'
    list_filter = ( 'author__first_name',)
    search_fields = ('title', 'detail', 'author__first_name')
    raw_id_fields = ('author',)
    date_hierarchy = 'created'
admin.site.register(UpFile,UpFileAdmin)

class FileAdmin(admin.ModelAdmin):
    list_display = ['upfile_id',]
admin.site.register(File,FileAdmin)

class MessageAdmin(admin.ModelAdmin):
    list_display = ['message_admin','title','created']
admin.site.register(Message,MessageAdmin)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth', 'photo']
admin.site.register(Profile, ProfileAdmin)