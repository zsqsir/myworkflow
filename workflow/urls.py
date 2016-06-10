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
    url(r'^relatedtable/$',views.relatedform,name='relatedform'),
    url(r'^application/$',views.application,name='application'),
    url(r'^reimbursement/$',views.creat_reimbursement,name='reimbursement'),
    url(r'^myreimbursement/$',views.myreimbursement,name='myreimbursement'),
    url(r'^p_reimbursement/$',views.p_reimbursement,name='p_reimbursement'),
]