from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import *
from django.http import HttpResponse,HttpResponseRedirect
from .models import *
from django.contrib import messages

@login_required
def index(request):
    content=dict(
        notices=Notices.objects.order_by('-updated')[0:5],
        myapplication=Leave_application.objects.filter(applicant=request.user),
    )
    return render(request,'process/index.html',content)

def register(request):
    if request.method == 'POST':
        register_form=UserRegistrationForm(request.POST)
        if register_form.is_valid():
            new_user=register_form.save(commit=False)
            new_user.set_password(register_form.cleaned_data['password'])
            new_user.save()
            messages.success(request,'注册成功')
            return HttpResponseRedirect('/index/')
        else:
            return HttpResponseRedirect('/register/')
    else:
        register_form=UserRegistrationForm()
        return render(request,'registration/register.html',{'register_form':register_form})

@login_required
def creat_form(request):
    content = dict(
        form=WorksheetForm(),
        person_name=Department.objects.filter(department_name=request.user.department.department_name),
    )
    if request.method=='POST':
        form=WorksheetForm(request.POST)
        if form.is_valid():
            form_save=form.save(commit=False)
            form_save.creater=request.user
            form_save.department=request.user.department
            form_save.who_is_processing=request.user.first_name
            form_save.related_person='，'.join(request.POST.getlist('person'))
            form_save.save()
            messages.success(request,'创建成功！')
        else:
            messages.error(request,'输入有误，请重试！')
    return render(request,'process/creat_form.html',content)
@login_required
def application(request):
    content = dict(
        application_form=Leave_application_Form()
    )
    if request.method=='POST':
        application_form=Leave_application_Form(request.POST)
        if application_form.is_valid():
            new_form=application_form.save(commit=False)
            new_form.applicant=request.user
            new_form.department=request.user.department
            new_form.save()
            messages.success(request,'创建成功！')
        else:
            messages.error(request,'填写有误请重试！')
    return render(request,'process/application.html',content)

@login_required
def myform(request):
    content=dict(
        myforms=worksheet.objects.filter(creater=request.user).order_by('-create_time'),
    )
    return render(request,'process/myform.html',content)

@login_required
def relatedform(request):
    content = dict(
        myforms=worksheet.objects.filter(related_person__contains=request.user.first_name).order_by('-create_time'),
        myprocesses=worksheet.objects.filter(who_is_processing=request.user.first_name),
        person_name=Department.objects.exclude(person=request.user).filter(department_name=request.user.department.department_name),
    )
    if request.method=='POST':
        if request.POST.get('change_person',False):
            date=request.POST.get('change_person',False).split('+')
            new_date=worksheet.objects.get(id=int(date[0]))
            new_date.who_is_processing=date[1]
            new_date.save()
            messages.success(request, '修改成功！')
        if request.POST.get('change_status',False):
            date=request.POST.get('change_status',False).split('+')
            new_date2=worksheet.objects.get(id=int(date[0]))
            new_date2.status_level=date[1]
            new_date2.save()
            messages.success(request, '修改成功！')
    return render(request,'process/related_form.html',content)

@login_required()
def creat_reimbursement(request):
    content=dict(
        form=ReimbursementForm()
    )
    if request.method == 'POST':
        reimbursementform=ReimbursementForm(request.POST)
        if reimbursementform.is_valid():
            new_form=reimbursementform.save(commit=False)
            new_form.department=request.user.department.department_name
            new_form.reimbursement_person=request.user
            new_form.save()
            messages.success(request,'成功')
        else:
            messages.error(request,'输入有误，检查后重试')
    return render(request,'process/reimbursement.html',content)

@login_required()
def myreimbursement(requset):
    content=dict(
        myforms=reimbursement.objects.filter(reimbursement_person=requset.user)
    )
    return render(requset,'process/myreimbursement.html',content)

@login_required()
def p_reimbursement(request):
    content=dict(
        myforms=reimbursement.objects.filter(status='未核准')
    )
    if request.method=='POST':
            date = request.POST.get('change_status', False)
            new_date = reimbursement.objects.get(id=int(date))
            new_date.status='审批通过'
            new_date.save()
    return render(request,'process/p_reimbursement.html',content)

def test(request):
    return render(request,'process/test.html')









#   使用自带的认证模块
# def log_in(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(username=username, password=password)
#         if user is not None:
#             if user.is_active:
#                 login( request,user)
#                 return HttpResponse('成功')
#             else:
#                 return HttpResponse('账户状态不正常')
#         else:
#             return HttpResponse('用户不存在')
#     else:
#         return render(request,'registration/login.html')

