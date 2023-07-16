from django.shortcuts import render,HttpResponse,redirect
from app01 import models
from app01.utils.bootstrap import BootstrapModelForm

class CityModelForm(BootstrapModelForm):
    bootstrap_exclude_fileds = ['logo']
    class Meta:
        model = models.City
        fields = "__all__"


def city_list(request):
    data_list = models.City.objects.all()
    return render(request,'city_list.html',{"data_list":data_list})

def city_add(request):
    title = "Add City"
    if request.method == 'GET':
        form = CityModelForm()
        return render(request, 'upload_form.html', {"form": form, "title": title})
    form = CityModelForm(data=request.POST, files=request.FILES)
    if form.is_valid():
        form.save()
        return redirect('/city/list')
    return render(request, 'upload_form.html', {"form": form, "title": title})