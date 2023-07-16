from django.shortcuts import render,HttpResponse,redirect
from django import forms
from app01.utils.bootstrap import BootstrapForm
from app01.utils.encrypt import md5
from app01.models import Admin
from app01.utils.code import check_code

class LoginForm(BootstrapForm):
    username = forms.CharField(label="username",widget=forms.TextInput,required=True)
    password = forms.CharField(label="password",widget=forms.PasswordInput(render_value=True), required=True)
    code = forms.CharField(label="Verification", widget=forms.TextInput,required=True)

    def clean_password(self):
        pwd = self.cleaned_data.get("password")
        return md5(pwd)

def login(request):
    if request.method =='GET':
        form = LoginForm()
        return render(request,'login.html',{"form":form})
    form = LoginForm(data=request.POST)
    if form.is_valid():
        user_input_code = form.cleaned_data.pop('code')
        if user_input_code.upper() != request.session.get('image_code').upper():
            form.add_error("code", "Incorrect Verification Code")
            return render(request, 'login.html', {"form": form})
        admin_obj = Admin.objects.filter(**form.cleaned_data).first()
        if not admin_obj:
            form.add_error("password","username and password doesn't match")
            return render(request, 'login.html', {"form": form})
        request.session['info'] = {'id':admin_obj.id,'name':admin_obj.username}
        return redirect('/admin/list')
    return render(request, 'login.html', {"form": form})

def logout(request):

    request.session.clear()

    return redirect('/login')

from io import BytesIO
def image_code(request):
    img, codestring = check_code()

    request.session['image_code'] = codestring
    request.session.set_expiry(60*60*24*7)

    stream = BytesIO()
    img.save(stream,'png')
    print(codestring)
    stream.getvalue()
    return HttpResponse(stream.getvalue())
