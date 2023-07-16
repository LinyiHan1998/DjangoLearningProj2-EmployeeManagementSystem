import os
from django.shortcuts import render,HttpResponse
from django.conf import settings
from django import forms
from app01.utils.bootstrap import BootstrapForm,BootstrapModelForm
from app01 import models
def upload_list(request):
    if request.method == 'GET':
        return render(request,'upload_list.html')
    print(request.POST)
    print(request.FILES)

    file_obj = request.FILES.get("avatar")
    f = open(file_obj.name, mode='wb')
    for chunk in file_obj.chunks():
        f.write(chunk)
    f.close()

    return HttpResponse("...")


class UpForm(BootstrapForm):
    name = forms.CharField(label='Name')
    age = forms.IntegerField(label='Age')
    image = forms.FileField(label='Avatar')
def upload_form(request):
    title = "Upload Form"
    if request.method == "GET":
        form = UpForm()
        return render(request,"upload_form.html",{"form":form,"title":title})
    form = UpForm(data=request.POST, files=request.FILES)
    if form.is_valid():
        #1.读取图片内容，写到文件夹中，并获取文件的路径
        img_obj = form.cleaned_data.get("image")


        #db_file_path = os.path.join(settings.MEDIA_ROOT,img_obj.name)
        #media_path = os.path.join(settings.MEDIA_ROOT,img_obj.name)
        media_path = os.path.join("media", img_obj.name)
        f = open(media_path,mode='wb')
        for chunk in img_obj.chunks():
            f.write(chunk)
        f.close()
        #2.将图片文件路径写入数据库
        models.Boss.objects.create(
            name=form.cleaned_data.get("name"),
            age=form.cleaned_data.get("age"),
            image=media_path,
        )
        return HttpResponse("...")
    return render(request,"upload_form.html",{"form":form,"title":title})

class UpModelForm(BootstrapModelForm):
    bootstrap_exclude_fileds = ['logo']
    class Meta:
        model = models.City
        fields = "__all__"
def upload_modelform(request):
    title = "Upload by ModelForm"
    if request.method =='GET':
        form = UpModelForm()
        return render(request,'upload_form.html',{"form":form,"title":title})
    form = UpModelForm(data = request.POST, files=request.FILES)
    if form.is_valid():
        form.save()
        return HttpResponse('...')
    return render(request, 'upload_form.html', {"form": form, "title": title})
