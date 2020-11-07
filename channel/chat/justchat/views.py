from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'chat/home.html')

def room(request,room_name):
    return render(request,'check/room.html',{'room_name':room_name})