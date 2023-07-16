from django.shortcuts import render,HttpResponse,redirect

from app01.models import Department,UserInfo,PrettyNum

from django import forms

from app01.utils.pagination import Pagination
def num_list(request):

    data_dict={}
    search_data = request.GET.get('q',"")
    if search_data:
        data_dict["mobile__contains"] = search_data

    querySet = PrettyNum.objects.filter(**data_dict).order_by('-level')

    page_obj = Pagination(request, querySet,search_data)
    page_queryset = page_obj.queryset
    page_string = page_obj.html()

    return render(request, 'num_list.html', {'page_queryset':page_queryset,"search_data":search_data,'page_string':page_string})

class NumModelForm(forms.ModelForm):
    class Meta:
        model = PrettyNum
        fields = ['id','mobile','price','level','status']
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        for name,field in self.fields.items():
            field.widget.attrs = {"class":"form-control" ,"placeholder":field.label}

def num_add(request):
    if request.method == 'GET':
        form = NumModelForm()
        return render(request,'num_add.html',{'form':form})
    form = NumModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/num/list')
    else:
        return render(request, 'num_add.html', {'form': form})

def num_edit(request,nid):
    queryset = PrettyNum.objects.filter(id=nid).first()
    if request.method =='GET':
        form = NumModelForm(instance = queryset)
        return render(request,'num_edit.html',{'form':form})
    form = NumModelForm(data=request.POST,instance=queryset)
    if form.is_valid():
        form.save()
        return redirect('/num/list')
    return render(request,'num_edit.html',{'form':form})

def num_delete(request,nid):
    PrettyNum.objects.filter(id = nid).delete()
    return redirect('/num/list')