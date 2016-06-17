from django.http import HttpResponseBadRequest

def ajax_required(fn):
    def wrap(request,*args,**kwargs):
        if not request.is_ajax():
            return HttpResponseBadRequest('<h1 style="margin-top: 18%;margin-left: 45%">禁止访问</h1></br><h1 style="margin-left: 45%">非法请求</h1>')
        return  fn(request,*args,**kwargs)
    wrap.__doc__=fn.__doc__
    wrap.__name__=fn.__name__
    return wrap