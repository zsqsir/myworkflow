from django.conf.urls import url
from . import views

urlpatterns=[
    url(r"test/$",views.test),
    # url(r'^login/$',views.log_in,name='login'),
    url(r'^index/$',views.index,name='index'),
    url(r'^$',views.index,name='index2'),
    url(r'^register/$',views.register,name='register'),
    url(r'^creat_form/$',views.creat_form,name='creat_form'),
    url(r'^myform/$',views.myform,name='myform'),
    url(r'^relatedform/$',views.relatedform,name='relatedform'),
    url(r'^application/$',views.application,name='application'),
    url(r'^reimbursement/$',views.creat_reimbursement,name='reimbursement'),
    url(r'^myreimbursement/$',views.myreimbursement,name='myreimbursement'),
    url(r'^p_reimbursement/$',views.p_reimbursement,name='p_reimbursement'),
    url(r'^upfile/$',views.upfile,name='upfile'),
    url(r'^myupfile/$',views.myupfile,name='myupfile'),
    url(r'^ctmessage/$',views.ctmessage,name='ctmessage'),
    url(r'^mymessage/$',views.mymessage,name='mymessage'),
    url(r'^message/(?P<mark_id>[0-9]+)/$',views.message_detail,name='message_detail'),
    url(r'^msg_ajax/$',views.msg_ajax,name='msg_ajax'),
    url(r'^msg_back_ajax/$',views.msg_back_ajax,name='msg_back_ajax'),
    url(r'^trash/$',views.trash,name='trash'),



]