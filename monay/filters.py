from django_filters.rest_framework import FilterSet
from .models import Endereco, Contato

class EnderecoFiltro(FilterSet):
    class Meta:
        model = Endereco
        fields = {
            'cliente':['exact']
        }

class ContatoFiltro(FilterSet):
    class Meta:
        model = Contato
        fields = {
            'cliente':['exact']
        }