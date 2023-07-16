from django.shortcuts import render,HttpResponse,redirect

from app01.models import Department,UserInfo,PrettyNum

from django import forms

from app01.utils.pagination import Pagination
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login')
def user_list(request):

    data_list = UserInfo.objects.all()
    page_obj = Pagination(request,data_list,'')
    page_query = page_obj.queryset
    page_string = page_obj.html()
    return render(request,'user_list.html',{"data":page_query,"page_string":page_string})

def user_add(request):
    if request.method == 'GET':
        context={
            'gender_choices': UserInfo.gender_choices,
            'depart_list': Department.objects.all(),
            'title':"Add User"
        }
        return render(request,'user_add.html',context)
    Title = request.POST.get("Title")
    Password = request.POST.get("Password")
    Age = request.POST.get("Age")
    Account = request.POST.get("Account")
    Employed_At = request.POST.get("Employed_At")
    Depart = request.POST.get("Department")
    Gender = request.POST.get("Gender")


    UserInfo.objects.create(name = Title,password=Password,age=Age,account=Account,create_time=Employed_At,gender=Gender,depart_id=Depart)
    return redirect("/user/list")


class UserModelForm(forms.ModelForm):

    class Meta:
        model = UserInfo
        fields = ["name","password","age","account","create_time","gender","depart"]
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        for name,field in self.fields.items():
            field.widget.attrs = {"class":"form-control" ,"placeholder":field.label}

def user_modeladd(request):
    if request.method =='GET':
        form = UserModelForm()
        return render(request, 'change.html', {"form": form,"title":"Add User"})
    form = UserModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect("/user/list")

    else:
        return render(request, 'user_modeladd.html', {"form": form})

def user_edit(request,nid):
    queryset = UserInfo.objects.filter(id=nid).first()
    if request.method == 'GET':
        form = UserModelForm(instance=queryset)

        return render(request,'user_edit.html', {'form':form})

    form = UserModelForm(data = request.POST,instance=queryset)

    if form.is_valid():
        form.save()
        return redirect('/user/list')
    return render(request,'user_edit.html',{'form':form})

def user_delete(request,nid):
    UserInfo.objects.filter(id=nid).delete()
    return redirect('/user/list')