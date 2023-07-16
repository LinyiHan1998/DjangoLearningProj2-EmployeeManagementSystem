from django import forms
from django.shortcuts import render,redirect
from django.core.exceptions import ValidationError
from app01.utils.bootstrap import BootstrapModelForm
from app01.models import Admin
from app01.utils.pagination import Pagination
from app01.utils.encrypt import md5

class AdminModelForm(BootstrapModelForm):
    confirm_password = forms.CharField(label="Confirm Password",
                                       widget=forms.PasswordInput)
    class Meta:
        model = Admin
        fields = ['username','password','confirm_password']
        widgets = {
            "password": forms.PasswordInput
        }
    def clean_password(self):
        pwd = self.cleaned_data.get("password")
        return md5(pwd)
    def clean_confirm_password(self):
        pwd = self.cleaned_data.get("password")
        confirm = md5(self.cleaned_data.get("confirm_password"))
        if pwd != confirm:
            raise ValidationError("Password doesn't match")
        return confirm

class AdminResetModelForm(BootstrapModelForm):

    confirm_password = forms.CharField(label="Confirm Password",
                                       widget=forms.PasswordInput)
    class Meta:
        model = Admin
        fields = ['password','confirm_password']
        widgets = {
            "password": forms.PasswordInput
        }

    def clean_password(self):
            pwd = self.cleaned_data.get("password")
            md5_pwd = md5(pwd)

            if Admin.objects.filter(id = self.instance.pk, password=md5_pwd).exists():
                raise ValidationError('Same as original password')
            return md5(pwd)

    def clean_confirm_password(self):
            pwd = self.cleaned_data.get("password")
            confirm = md5(self.cleaned_data.get("confirm_password"))
            if pwd != confirm:
                raise ValidationError("Password doesn't match")
            return confirm
def admin_list(request):
    data_dict={}
    search_data = request.GET.get('q',"")
    if search_data:
        data_dict["username__contains"] = search_data
    queryset = Admin.objects.filter(**data_dict)
    page_obj = Pagination(request,queryset,search_data)
    page_queryset = page_obj.queryset
    page_string = page_obj.html()
    return render(request,'admin_list.html',{'page_queryset':page_queryset,'page_string':page_string})

def admin_add(request):
    if request.method =='GET':
        form = AdminModelForm()
        return render(request,'change.html',{"title":"Add Admin","form":form})

    form = AdminModelForm(data=request.POST )

    if form.is_valid():
        form.save()
        return redirect('/admin/list')
    return render(request, 'change.html', {"title": "Add Admin", "form": form})

def admin_edit(request,nid):
    row_obj = Admin.objects.filter(id=nid).first()
    if not row_obj:
        return redirect('/admin/list')

    if request.method == 'GET':
        form = AdminModelForm(instance=row_obj)
        return render(request, 'change.html', {"title": "Edit Admin", "form": form})

    form = AdminModelForm(data=request.POST,instance=row_obj)

    if form.is_valid():
        form.save()
        return redirect('/admin/list')
    return render(request, 'change.html', {"title": "Edit Admin", "form": form})

def admin_delete(request,nid):
    row_obj = Admin.objects.filter(id=nid).first().delete()
    return redirect('/admin/list')

def admin_reset(request,nid):
    row_obj = Admin.objects.filter(id=nid).first()
    if not row_obj:
        return redirect('/admin/list')

    title = "Reset Password - {}".format(row_obj.username)
    if request.method == 'GET':
        form = AdminResetModelForm(instance=row_obj)
        return render(request, 'change.html', {"title": title, "form": form})

    form = AdminResetModelForm(data=request.POST, instance=row_obj)

    if form.is_valid():
        form.save()
        return redirect('/admin/list')
    return render(request, 'change.html', {"title": "Reset Password", "form": form})