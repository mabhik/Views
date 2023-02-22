from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from app.forms import *
# Create your views here.

def FbvS(request):
    return HttpResponse('function based view')

class CbvS(View):
    def get(self,request):
        return HttpResponse('class based view')

def FbvH(request):
    d={'today':'shivarathri'}
    return render(request, 'FbvH.html',d)

class CbvH(View):
    def get(self,request):
        d={'festival':'mahashivarathri'}
        return render(request,'CbvH.html',d)

def FbvdF(request):
    sfo=student()
    d={'sfo':sfo}
    if request.method=='POST':
        sfd=student(request.POST)
        if sfd.is_valid():
            return HttpResponse(str(sfd.cleaned_data))
    return render(request,'FbvdF.html',d)

class CbvdF(View):
    def get(self,request):
        sfo=student()
        d={'sfo':sfo}
        return render(request,'CbvdF.html',d)

    def post(self,request):
        sfd=student(request.POST)
        if sfd.is_valid():
            return HttpResponse(str(sfd.cleaned_data))