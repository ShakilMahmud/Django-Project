from django.urls import path
from .import views

urlpatterns=[
    path('',views.show_todo),
    path('addtodo/',views.add)
]