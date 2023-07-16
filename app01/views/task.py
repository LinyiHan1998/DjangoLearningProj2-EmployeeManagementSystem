import json
from django.shortcuts import render,HttpResponse
from django import forms
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.forms.utils import ErrorDict
from app01.utils.bootstrap import BootstrapModelForm
from app01 import models

class taskModelForm(BootstrapModelForm):
    class Meta:
        model = models.Task
        fields = "__all__"
        widgets = {
            "detail" : forms.TextInput
        }

def task_list(request):
    form = taskModelForm()
    return render(request, 'task_list.html',{"form":form})

@csrf_exempt
def task_ajax(request):
    print(request.POST)
    data_dict = {
        "status": True,
        'data':[11,22,33,44]
    }
    #json_string = json.dumps(data_dict)
    return JsonResponse(data_dict)
@csrf_exempt
def task_add(request):
    print(request.POST)
    form = taskModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        data_dict = {
            "status": True,
        }
        # json_string = json.dumps(data_dict)
        return JsonResponse(data_dict)
    data_dict = {
        "status": False,
        "error": form.errors
    }
    json_string = json.dumps(data_dict,ensure_ascii=False)
    return HttpResponse(json_string)