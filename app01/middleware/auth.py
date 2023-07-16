from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect

class AuthMiddleware(MiddlewareMixin):

    #0. 排除不需要登录就可以访问的页面
    #request.path_info 获取当前用户请求的urls

    def process_request(self,request):
        if request.path_info in ["/login/","/image/code/"]:
            return
        #1. 读取当前访问用户的session信息，如果能读到说明已经登陆，可以继续向后
        info_dict = request.session.get("info")
        if info_dict:
            return
        #2. 没有登录
        return redirect('/login/')
    def process_response(self,request,response):
        return response

