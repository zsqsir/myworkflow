
from .models import worksheet,reimbursement,Message,File,UpFile

def worksheet_num(request):
    if request.user.is_active:
        num = worksheet.objects.filter(related_person__contains=request.user.first_name).count()
        num2=reimbursement.objects.filter(reimbursement_person=request.user).count()
        return {'num': num,'num2':num2}
    else:
        return {}

def worksheet_percent(request):
    if request.user.is_active:
        a_percent = worksheet.objects.filter(related_person__contains=request.user.first_name)
        b_percent = a_percent.filter(status_level='审批通过').count()
        if a_percent and b_percent:
            percent= '%.2f%%'%((b_percent/a_percent.count())*100)
        # percent = b_percent / a_percent.count()
            return {'percent': percent}
        else:
            return {}
    else:
        return {}
def percent(request):
    if request.user.is_active:
        c_percent = reimbursement.objects.filter(reimbursement_person=request.user)
        d_percent = c_percent.filter(status='审批通过').count()
        if c_percent and d_percent:
            percent2 = '%.2f%%' % ((d_percent / c_percent.count()) * 100)
            return {'percent2': percent2}
        else:
            return {}
    else:
        return {}

def new_message_num(request):
    if request.user.is_active:
        new_message=Message.objects.filter(to_user=request.user,accept_msg_status=1).count()
        if new_message != 0:
            return {'new_message':new_message}
        else:
            return {'new_message':''}
    else:
        return {}


def file_count(request):
    if request.user.is_active:
        file_num=UpFile.objects.filter(author=request.user,status='等待审核').count()
        if file_num !=0:
            return {"file_num":file_num}
        else:
            return {"file_num": ''}
    else:
        return {}