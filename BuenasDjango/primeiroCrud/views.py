from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from .models import Pessoa
from .forms import PessoaCreateForm 
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import PessoaSerializer
from .models import Pessoa
# Create your views here.
#criação da tela de cadastro de pessoa
class PessoaCreateView(CreateView):
    model = Pessoa
    form_class = PessoaCreateForm
    template_name = 'cadastrar_pessoa.html'
    success_url = reverse_lazy('lista_pessoas')


class PessoaListView(ListView):
    model = Pessoa 
    template_name = 'lista_pessoas.html'
# Create your views here.

class PessoaViewSet(viewsets.ModelViewSet):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True) 

        # Adicionar lógica extra aqui, se necessário
        # Atualiza os dados no banco de dados
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to  
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data) 