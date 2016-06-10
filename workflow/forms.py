from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from .models import *
from django.forms.extras.widgets import SelectDateWidget

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='密码',widget=forms.PasswordInput)
    password2 = forms.CharField(label='再次输入',widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')
        labels = {
            'username': _('用户名'),
            'email': _('邮箱地址'),
            'first_name': _('名字'),
        }
        help_texts = {
            'first_name': _('名字（必填）'),
        }
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('两次输入的密码不一样，请重试.')
        return cd['password2']

class WorksheetForm(forms.ModelForm):
    class Meta:
        model=worksheet
        exclude=('creater','department','who_is_processing','related_person')
        widgets = {
            'plan_finish_time': SelectDateWidget,
        }

class Leave_application_Form(forms.ModelForm):
    class Meta:
        model=Leave_application
        exclude=('applicant','department','reply','status')
        widgets = {
            'start_date': SelectDateWidget,
            'finished_date': SelectDateWidget,
        }
class ReimbursementForm(forms.ModelForm):
    def test_num(self):
        num = self.cleaned_data['money']
        if float(num) < 0:
            raise forms.ValidationError('金额错误，检查后重试')
        else:
            return num
    class Meta:
        model = reimbursement
        exclude=('reimbursement_person','department','status')
        widgets={
            'start_date': SelectDateWidget,
            'end_date': SelectDateWidget,
        }
