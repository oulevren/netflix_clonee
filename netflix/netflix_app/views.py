from django.shortcuts import render

# Create your views here.

#anasayfa
def index(request):
    return render(request,"index.html")