from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializer import UsuarioSerializer, ClienteSerializer 
from .serializer import EmprestimoSerializer, ContatoSerializer, EnderecoSerializer
from .serializer import PgtoEmprestimoSerializer, ContaSerializer
from .serializer import FavoritoSerializer, ExtratoSerializer, TransacaoSerializer
from .serializer import CartaoSerializer, FaturaSerializer
from .models import Cliente, Usuario, Contato, Endereco
from .models import PgtoEmprestimo, Emprestimo, Conta, Favorito
from .models import Extrato, Transacao, Cartao, Fatura
from rest_framework.response import Response
from datetime import datetime
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .filters import EnderecoFiltro, ContatoFiltro
# Create your views here.

# class FotoInViewSet(viewsets.ModelViewSet):
#     queryset = Cliente.objects.filter(fotoCliente)
#     serializer_class = FotoInSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    # def update(self, request, pk=id):
    #     anoCliente = str(request.data['dataNascimento'])
    #     anoCliente = anoCliente[0:4]
    #     if int(datetime.now().year) - (int(anoCliente)) < 18:
    #         return Response({
    #             'erro':'o cliente deve possuir mais de 18 anos.'
    #         })
    #     return super().update(self, request, pk=id)

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    # class ClienteDetalhes(RetrieveUpdateDestroyAPIView):
    #     queryset = Cliente.objects.all()
    #     serializer_class = ClienteSerializer
    #     def update(self, request, *args, **kwargs):
    #         dataCliente = str(request.data['dataNascimento'])
    #         anoCliente = dataCliente[0:4]
    #         mesCliente = dataCliente[6:7]
    #         diaCliente = dataCliente[9:10]
    #         print(anoCliente)
    #         if int(datetime.now().year) - (int(anoCliente)) < 18:
    #             # if (int(mesCliente) > int(datetime.now().month)): 
    #             #     return Response({
    #             #         'erro':'o cliente deve possuir mais de 18 anos.'
    #             #     })
    #             # elif (int(mesCliente) == int(datetime.now().month)):
    #             #     if (int(diaCliente) > int(datetime.now().day)):
    #             #         return Response({
    #             #             'erro':'o cliente deve possuir mais de 18 anos.'
    #             #         })
    #             return Response({
    #                 'erro':'o cliente deve possuir mais de 18 anos.'
    #             })
    #         return super().update(request, *args, **kwargs)

class PgtoEmprestimoViewSet(viewsets.ModelViewSet):
    queryset = PgtoEmprestimo.objects.all()
    serializer_class = PgtoEmprestimoSerializer

class EmprestimoViewSet(viewsets.ModelViewSet):
    queryset = Emprestimo.objects.all()
    serializer_class = EmprestimoSerializer

class EnderecoViewSet(viewsets.ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = EnderecoFiltro

class ContatoViewSet(viewsets.ModelViewSet):
    queryset = Contato.objects.all()
    serializer_class = ContatoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ContatoFiltro

class ContaViewSet(viewsets.ModelViewSet):
    queryset = Conta.objects.all()
    serializer_class = ContaSerializer

class FavoritoViewSet(viewsets.ModelViewSet):
    queryset = Favorito.objects.all()
    serializer_class = FavoritoSerializer

class ExtratoViewSet(viewsets.ModelViewSet):
    queryset = Extrato.objects.all()
    serializer_class = ExtratoSerializer

class TransacaoViewSet(viewsets.ModelViewSet):
    queryset = Transacao.objects.all()
    serializer_class = TransacaoSerializer

class CartaoViewSet(viewsets.ModelViewSet):
    queryset = Cartao.objects.all()
    serializer_class = CartaoSerializer

class FaturaViewSet(viewsets.ModelViewSet):
    queryset = Fatura.objects.all()
    serializer_class = FaturaSerializer
