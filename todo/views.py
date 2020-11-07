from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
def show_todo(request):
    return render(request,'todo_page.html')

def add(request):
    all_item='hello'
    return render(request,'todo_page.html',{'all':all_item})