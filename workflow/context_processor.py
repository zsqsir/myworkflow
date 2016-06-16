
from .models import worksheet,reimbursement

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