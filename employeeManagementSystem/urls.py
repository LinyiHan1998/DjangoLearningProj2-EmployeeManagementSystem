"""
URL configuration for employeeManagementSystem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from django.views.static import serve
from django.conf import settings
from app01.views import number,user,depart,admin,account,task,order,chart,upload,city

urlpatterns = [
    re_path(r'media/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT},name='media'),
    #path('admin/', admin.site.urls),
    #部门管理
    path('depart/list/', depart.depart_list),
    path('depart/add/', depart.depart_add),
    path('depart/delete/', depart.depart_delete),
    path('depart/<int:nid>/edit/', depart.depart_edit),
    path('depart/multi', depart.depart_multi),

    #用户管理
    path('user/list', user.user_list),
    path('user/add/', user.user_add),
    path('user/modeladd/', user.user_modeladd),
    path('user/<int:nid>/delete/', user.user_delete),
    path('user/<int:nid>/edit/', user.user_edit),

    #靓号管理
    path('num/list', number.num_list),
    path('num/add/', number.num_add),
    path('num/<int:nid>/edit/', number.num_edit),
    path('num/<int:nid>/delete/', number.num_delete),

    #管理员
    path('admin/list', admin.admin_list),
    path('admin/add/', admin.admin_add),
    path('admin/<int:nid>/edit/', admin.admin_edit),
    path('admin/<int:nid>/delete/', admin.admin_delete),
    path('admin/<int:nid>/reset/', admin.admin_reset),

    #登录
    path('login/', account.login),
    path('logout/', account.logout),
    path('image/code/', account.image_code),

    # 任务管理 测试ajax
    path('task/list', task.task_list),
    path('task/ajax', task.task_ajax),
    path('task/add', task.task_add),

    #订单管理
    path('order/list', order.order_list),
    path('order/add', order.order_add),
    path('order/delete/', order.order_delete),
    path('order/detail',order.order_detail),
    path('order/edit/',order.order_edit),

    #数据统计
    path('chart/list',chart.chart_list),
    path('chart/col',chart.chart_col),

    #上传文件
    path('upload/list',upload.upload_list),
    path('upload/form',upload.upload_form),
    path('upload/modelform',upload.upload_modelform),

    #城市列表
    path('city/list',city.city_list),
    path('city/add',city.city_add),
]
