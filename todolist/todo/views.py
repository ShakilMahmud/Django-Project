from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import todom

# Create your views here.
def show(request):
    data =todom.objects.all()
    return render(request,'home.html',{'data':data})

def add(request):
    tododata=request.POST['todo']
    todo_item=todom(content=tododata)
    todo_item.save()
    return redirect(show)

def delete(request,todo_id):
    item=todom.objects.get(id=todo_id)
    item.delete()
    return redirect(show)

