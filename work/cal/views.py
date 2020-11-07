from django.shortcuts import render
from django.http import HttpResponse
def calc(request):
    return render(request,'base.html')

def show(request):
    return render(request,'beast.html')

def result(request):
    num1=request.POST['first'] 
    num2=request.POST['second']
    res=int(num1) + int(num2)

    return render(request,'result.html',{'result' : res})