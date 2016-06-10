from django.db import models
from django.contrib.auth.models import User

class Notices(models.Model):
    title=models.CharField('标题',max_length=30)
    content=models.TextField('内容')
    created=models.DateTimeField('发布时间',auto_now_add=True)
    updated=models.DateTimeField('更新时间',auto_now=True)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name='公告'
        verbose_name_plural='公告'

class Department(models.Model):
    person=models.OneToOneField(User,related_name='department',verbose_name='姓名')
    department_choise=(
        ('业务部','业务部'),
        ('财务部','财务部'),
    )
    level_choise=(
        ('经理','经理'),
        ('职员','职员'),
    )
    department_name=models.CharField('部门',max_length=20,choices=department_choise)
    level=models.CharField('职位',max_length=10,choices=level_choise)
    def __str__(self):
        return self.department_name
    def person_name(self):
        return self.person.first_name
    person_name.short_description = '姓名'
    class Meta:
        verbose_name='行政部门'
        verbose_name_plural='行政部门'

class Leave_application(models.Model):
    status_choise=(
        ('等待批准','等待批准'),
        ('批准','批准'),
        ('不批准','不批准'),
    )

    applicant=models.ForeignKey(User,related_name='leave_application',verbose_name='申请人')
    title=models.CharField('标题',max_length=50)
    start_date=models.DateField('开始时间')
    finished_date=models.DateField('结束时间')
    reason=models.TextField('请假因由')
    status=models.CharField('申请状态',choices=status_choise,default='等待批准',max_length=10)
    reply=models.TextField('批复',max_length=250,blank=True)
    department=models.CharField('部门',max_length=20)
    def applicant_name(self):
        return self.applicant.first_name
    applicant_name.short_description = '申请人'
    class Meta:
        verbose_name='请假'
        verbose_name_plural='请假'

class worksheet(models.Model):
    status_now=(
        ('修改中','修改中'),
        ('验证中','验证中'),
        ('审批中','审批中'),
    )

    creater=models.ForeignKey(User,related_name='worksheet',verbose_name='创建人')
    title=models.CharField('标题',max_length=20)
    description=models.TextField('情况说明',max_length=300)
    who_is_processing=models.CharField('当前处理人',max_length=20,default='未知')
    create_time=models.DateField('创建时间',auto_now_add=True)
    plan_finish_time=models.DateField('计划完成时间')
    related_person=models.CharField('相关人员',max_length=100)
    status_level=models.CharField('当前状态',max_length=10,choices=status_now,default='修改中')
    department=models.CharField('部门',max_length=20)
    def __str__(self):
        return self.title
    def worksheet_person(self):
        return "%s的工单" % self.creater.first_name
    worksheet_person.short_description = '工单'
    class Meta:
        verbose_name='工单'
        verbose_name_plural='工单'

class reimbursement(models.Model):
    reimbursement_person=models.ForeignKey(User,related_name='reimbursement',verbose_name='报销人')
    titile=models.CharField('报销单',max_length=30,default='报销')
    start_date=models.DateField('开始时间')
    end_date=models.DateField('结束时间')
    description = models.TextField('情况说明', max_length=300,help_text='报销的内容')
    money=models.FloatField('金额')
    status=models.CharField('审批状态',default='未核准',max_length=20)
    department=models.CharField('部门',max_length=10)
    def __str__(self):
        return self.titile
    def reimbursement_of_person(self):
        return "%s的报销" % self.reimbursement_person.first_name
    reimbursement_of_person.short_description='报销申请'
    class Meta:
        verbose_name='报销管理'
        verbose_name_plural='报销管理'

