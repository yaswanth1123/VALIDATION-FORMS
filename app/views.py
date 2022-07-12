from django.shortcuts import render
from django.http import HttpResponse
from app.forms import *

# Create your views here.
def validating(request):
    NF=NameForm()
    d={'NF':NF}

    if request.method=='POST':
        FD=NameForm(request.POST)
        if FD.is_valid():
            return HttpResponse('valid form')
    return render(request,'validating.html',d)