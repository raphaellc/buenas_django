from django import forms
from .models import Pessoa

class PessoaCreateForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = '__all__' # alternativa para usar todos os campos -> '__all__'
