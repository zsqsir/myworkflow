from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import *
from django.http import HttpResponseRedirect, JsonResponse,HttpResponse
from .models import *
from django.contrib import messages
from .common.decorators import ajax_required
from django.views.decorators.http import require_POST

@login_required
def index(request):
    content = dict(
        notices=Notices.objects.order_by('-updated')[0:5],
        myapplication=Leave_application.objects.filter(applicant=request.user),
    )
    return render(request, 'process/index.html', content)

def register(request):
    if request.method == 'POST':
        register_form = UserRegistrationForm(request.POST)
        if register_form.is_valid():
            new_user = register_form.save(commit=False)
            new_user.set_password(register_form.cleaned_data['password'])
            new_user.save()
            messages.success(request, '注册成功')
            return HttpResponseRedirect('/index/')
        else:
            return HttpResponseRedirect('/register/')
    else:
        register_form = UserRegistrationForm()
        return render(request, 'registration/register.html', {'register_form': register_form})


@login_required
def creat_form(request):
    content = dict(
        form=WorksheetForm(),
        person_name=Department.objects.filter(department_name=request.user.department.department_name),
    )
    if request.method == 'POST':
        form = WorksheetForm(request.POST)
        if form.is_valid():
            form_save = form.save(commit=False)
            form_save.creater = request.user
            form_save.department = request.user.department
            form_save.who_is_processing = request.user.first_name
            form_save.related_person = '，'.join(request.POST.getlist('person'))
            form_save.save()
            messages.success(request, '创建成功！')
        else:
            messages.error(request, '输入有误，请重试！')
    return render(request, 'process/creat_form.html', content)


@login_required
def application(request):
    content = dict(
        application_form=Leave_application_Form()
    )
    if request.method == 'POST':
        application_form = Leave_application_Form(request.POST)
        if application_form.is_valid():
            new_form = application_form.save(commit=False)
            new_form.applicant = request.user
            new_form.department = request.user.department
            new_form.save()
            messages.success(request, '创建成功！')
        else:
            messages.error(request, '填写有误请重试！')
    return render(request, 'process/application.html', content)

@login_required
def myform(request):
    content = dict(
        myforms=worksheet.objects.filter(creater=request.user).order_by('-create_time'),
    )
    return render(request, 'process/myform.html', content)


@login_required
def relatedform(request):
    content = dict(
        myforms=worksheet.objects.filter(related_person__contains=request.user.first_name),
        myprocesses=worksheet.objects.filter(who_is_processing=request.user.first_name),
        person_name=Department.objects.exclude(person=request.user).filter(
            department_name=request.user.department.department_name),
    )
    if request.method == 'POST':
        if request.POST.get('change_person', False):
            date = request.POST.get('change_person', False).split('+')
            new_date = worksheet.objects.get(id=int(date[0]))
            new_date.who_is_processing = date[1]
            new_date.save()
            messages.success(request, '修改成功！')
        if request.POST.get('change_status', False):
            date = request.POST.get('change_status', False).split('+')
            new_date2 = worksheet.objects.get(id=int(date[0]))
            new_date2.status_level = date[1]
            new_date2.save()
            messages.success(request, '修改成功！')
    return render(request, 'process/related_form.html', content)


@login_required
def creat_reimbursement(request):
    content = dict(
        form=ReimbursementForm()
    )
    if request.method == 'POST':
        reimbursementform = ReimbursementForm(request.POST)
        if reimbursementform.is_valid():
            new_form = reimbursementform.save(commit=False)
            new_form.department = request.user.department.department_name
            new_form.reimbursement_person = request.user
            new_form.save()
            messages.success(request, '成功')
        else:
            messages.error(request, '输入有误，检查后重试')
    return render(request, 'process/reimbursement.html', content)


@login_required
def myreimbursement(requset):
    content = dict(
        myforms=reimbursement.objects.filter(reimbursement_person=requset.user)
    )
    return render(requset, 'process/myreimbursement.html', content)


@login_required
def p_reimbursement(request):
    content = dict(
        myforms=reimbursement.objects.filter(status='未核准')
    )
    if request.method == 'POST':
        date = request.POST.get('change_status', False)
        new_date = reimbursement.objects.get(id=int(date))
        new_date.status = '审批通过'
        new_date.save()
    return render(request, 'process/p_reimbursement.html', content)


@login_required
def upfile(request):
    content = dict(
        upfileform=UpFileForm(),
        myfileform=MyfileForm(),
    )
    if request.method == 'POST':
        upfileform = UpFileForm(request.POST)  # ,request.FILES
        myfileform = MyfileForm(request.POST, request.FILES)
        if upfileform.is_valid() and myfileform.is_valid():
            extent = upfileform.save(commit=False)
            extent.author = request.user
            extent.save()
            newfile = myfileform.save(commit=False)
            newfile.file_id = extent
            newfile.save()
            messages.success(request, '上传成功')
        else:
            messages.error(request, '上传失败，检查后重试')
    return render(request, 'process/upfile.html', content)


@login_required
def myupfile(request):
    content = dict(
        myfiles=UpFile.objects.filter(author=request.user).order_by('-update'),
        myfileform=MyfileForm(),
    )
    if request.method == 'POST':
        id_num = request.POST['id']
        id = UpFile.objects.get(id=id_num)

        myfileform = MyfileForm(request.POST, request.FILES)
        if myfileform.is_valid():
            new_form = myfileform.save(commit=False)
            new_form.file_id = id
            new_form.save()
            messages.success(request, '上传成功')
        else:
            messages.error(request, '上传失败，检查后重试')
    return render(request, 'process/myupfile.html', content)

@ajax_required
@login_required
@require_POST
def search(request):
    if request.POST.get('value'):
        value=request.POST.get('value')
        content=dict(
            myfiles=File.objects.filter(file_name__contains=value)
        )
        return render(request,'process/search.html',content)
    else:
        return JsonResponse({"status":"输入有误"})


@login_required
def ctmessage(request):
    content = dict(
        form=MessageForm(),
    )
    if request.method == 'POST':
        new_form = MessageForm(request.POST)
        if new_form.is_valid():
            new_message = new_form.save(commit=False)
            new_message.from_user = request.user
            new_message.save()
            new_message.up_id()
            messages.success(request, '发送成功')
        else:
            messages.error(request, '发送失败')
    return render(request, 'process/creat_message.html', content)


@login_required
def mymessage(request):
    content = dict(
        messages_from=Message.objects.filter(to_user=request.user).exclude(accept_msg_status__in=[0, 3]),
        messages_to=Message.objects.filter(from_user=request.user).exclude(sender_msg_status__in=[0, 3]),
    )
    return render(request, 'process/mymessage.html', content)


@login_required
def message_detail(request, mark_id):
    content = dict(
        message=Message.objects.filter(marks=mark_id),
    )
    if request.method == 'POST':
        user = User.objects.get(id=request.POST['to_user'])
        msg = Message(from_user=request.user, to_user=user, title=request.POST['title'], marks=request.POST['mark_id'],
                      content=request.POST['msg'])
        msg.save()
        messages.success(request, '成功')
    return render(request, 'process/message_detail.html', content)


@ajax_required
@login_required
@require_POST
def msg_ajax(request):
    if request.POST.get('accept_id'):
        id = request.POST.get('accept_id')
        msg = Message.objects.get(id=int(id))
        msg.accept_msg_status = 0
        msg.save()
        return JsonResponse({'status': "ok"})
    if request.POST.get('send_id'):
        id = request.POST.get('send_id')
        msg = Message.objects.get(id=int(id))
        msg.sender_msg_status = 0
        msg.save()
        return JsonResponse({'status': "删除成功"})
    if request.POST.get('new_msg_id'):
        id = request.POST.get('new_msg_id')
        msg = Message.objects.get(id=int(id))
        msg.accept_msg_status = 2
        msg.save()
        return JsonResponse({'status': "成功"})
    else:
        return JsonResponse({"status": "wrong value"})

@ajax_required
@login_required
@require_POST
def msg_back_ajax(request):
    if request.POST.get('msg_from_back_id'):
        id = request.POST.get('msg_from_back_id')
        msg = Message.objects.get(id=id)
        msg.accept_msg_status = 2
        msg.save()
        return JsonResponse({'status': "删除成功"})
    if request.POST.get('msg_to_back_id'):
        id = request.POST.get('msg_to_back_id')
        msg = Message.objects.get(id=id)
        msg.sender_msg_status = 2
        msg.save()
        return JsonResponse({'status': "删除成功"})
    if request.POST.get('msg_from_del_id'):
        id = request.POST.get('msg_from_del_id')
        msg = Message.objects.get(id=id)
        msg.accept_msg_status = 3
        msg.save()
        return JsonResponse({'status': "删除成功"})
    if request.POST.get('msg_to_del_id'):
        id = request.POST.get('msg_to_del_id')
        msg = Message.objects.get(id=id)
        msg.sender_msg_status = 3
        msg.save()
        return JsonResponse({'status': "删除成功"})

    else:
        return JsonResponse({"status": "wrong value"})


@login_required
def trash(request):
    content = dict(
        trash_from=Message.objects.filter(to_user=request.user, accept_msg_status=0),
        trash_to=Message.objects.filter(from_user=request.user, sender_msg_status=0)
    )
    return render(request, 'process/trash.html', content)


def test(request,a):
    b=1
    return HttpResponse(b)

def my404(request):
    return render(request,'process/error404.html')

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
