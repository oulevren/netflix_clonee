from django.shortcuts import render,redirect
from .forms import *

# Create your views here.

def register_page(request):
    context = {}
    context["registerForm"] = UserForm

    if request.method == 'POST':
        form = UserForm(request.POST)

        #form geçerli mi değil mi
        if form.is_valid():
            #veritabanına kaydet
            form.save()
            #logine yönlendir
            return redirect('page-index')
        else:
            #hata ver
            print("FORM HATAASI",form.errors)
            # return redirect('page-register')
            context["errorForm"] = form.errors
            return render(request,"register.html",context)

    else:
        #get ise sayfayı hazırla
        # context["registerForm"] = UserForm
        return render(request,"register.html",context)
    

def login_page(request):
    return render(request,"login.html")