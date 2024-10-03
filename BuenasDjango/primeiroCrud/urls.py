from django.urls import path
from django.http import HttpResponse
from .views import PessoaCreateView, PessoaListView
 

def primeiroCrud(request):
    return HttpResponse('Primeiro App')

urlpatterns = [
    path('',primeiroCrud),
    path('cadastrar_pessoa/', PessoaCreateView.as_view(), name='cadastrar_pessoa'),
    path('listar_pessoa/', PessoaListView.as_view(), name='lista_pessoas'),
]