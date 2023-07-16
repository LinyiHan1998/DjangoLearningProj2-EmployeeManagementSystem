import json
import random
from datetime import datetime
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from app01 import models
from app01.utils.bootstrap import BootstrapModelForm
from app01.utils.pagination import Pagination


class OrderModelForm(BootstrapModelForm):
    class Meta:
        model = models.Order
        #fields = "__all__"
        exclude = ["Oid","admin"]

def order_list(request):
    queryset = models.Order.objects.all().order_by('-id')
    page = Pagination(request,queryset,'')
    form = OrderModelForm()

    context = {
        'form':form,
        "queryset":page.queryset,
        'page_string':page.html(),
    }
    form = OrderModelForm()
    return render(request,'order_list.html',context)

@csrf_exempt
def order_add(request):
    # print(request.POST)
    # form = OrderModelForm(data=request.POST)
    # if form.is_valid():
    #     form.save()
    #     data_dict = {
    #         "status": True,
    #     }
    #     # json_string = json.dumps(data_dict)
    #     return JsonResponse(data_dict)
    # data_dict = {
    #     "status": False,
    #     "error": form.errors
    # }
    # #json_string = json.dumps(data_dict,ensure_ascii=False)
    # return JsonResponse(data_dict)

    print(request.POST)
    form = OrderModelForm(data=request.POST)

    if form.is_valid():
        form.instance.Oid = datetime.now().strftime("%Y%m%d%H%M%S") + str(random.randint(1000,9999))
        form.instance.admin_id = request.session["info"]["id"]
        form.save()
        data_dict = {
            "status": True,
        }
        #data_string = json.dumps(dataset,ensure_ascii=False)
        return JsonResponse(data_dict)
    data_dict = {
        "status": False,
        "error": form.errors
    }
    #data_string = json.dumps(data_dict, ensure_ascii=False)
    return JsonResponse(data_dict)

def order_delete(request):
    uid = request.GET.get("uid")
    if models.Order.objects.filter(id=uid).exists():
        models.Order.objects.filter(id=uid).delete()
        return JsonResponse({"status":True})
    return JsonResponse({"status": False, "error": "data doesn't exist"})

def order_detail(request):

    #新办法，使用values()获取到想要的列的字典

    uid = request.GET.get("uid")
    row_dict = models.Order.objects.filter(id=uid).values("title","price","status").first()
    if not row_dict:
        return JsonResponse({"status":False,"error":"data doesn't exists"})
    result = {
        "status":True,
        "data":row_dict,
    }
    return JsonResponse(result)
    #旧办法，获取到整个对象
    # uid = request.GET.get("uid")
    # row_obj = models.Order.objects.filter(id=uid).first()
    # if not row_obj:
    #     return JsonResponse({"status":False,"error":"data doesn't exists"})
    # result = {
    #     "status":True,
    #     "data":{
    #         "title":row_obj.title,
    #         "price":row_obj.price,
    #         "status":row_obj.status,
    #     }
    # }
    # return JsonResponse(result)

@csrf_exempt
def order_edit(request):
    uid = request.GET.get("uid")
    print(uid)
    row_obj = models.Order.objects.filter(id=uid).first()
    if not row_obj:
        return JsonResponse({"status":False,"tips":"data doesn't exists"})

    form = OrderModelForm(data = request.POST, instance=row_obj)
    if form.is_valid():
        form.save()
        return JsonResponse({"status":True})
    return JsonResponse({"status":False,"error":form.errors})

