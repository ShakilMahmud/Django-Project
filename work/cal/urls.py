from django.urls import path
from . import views
urlpatterns=[
    path('',views.show),
    path('cal/',views.calc),
    path('cal/add',views.result),
]