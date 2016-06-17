from django import template
from django.template.defaultfilters import stringfilter
register = template.Library()

@register.filter
@stringfilter
def filename(value):
    return value.split('/')[-1]

@register.filter
def my_order_by(queryset,args):
    args = [x.strip() for x in args.split(',')]
    return queryset.order_by(*args)

@register.filter
def static_file(add):
    return '/static/file/'+str(add)