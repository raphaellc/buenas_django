from django.urls import path
from django.http import HttpResponse

def primeiroCrud(request):
    return HttpResponse('Primeiro App')

urlpatterns = [
    path('',primeiroCrud),
]