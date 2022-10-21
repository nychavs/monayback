from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register('usuario', views.UsuarioViewSet)
router.register('cliente', views.ClienteViewSet)
router.register('emprestimo', views.EmprestimoViewSet)
router.register('pgtoemprestimo', views.PgtoEmprestimoViewSet)
router.register('endereco', views.EnderecoViewSet)
router.register('contato', views.ContatoViewSet)
router.register('conta', views.ContaViewSet)
router.register('favorito', views.FavoritoViewSet)
router.register('extrato', views.ExtratoViewSet)
router.register('transacao', views.TransacaoViewSet)
router.register('cartao', views.CartaoViewSet)
router.register('fatura', views.FaturaViewSet)
urlpatterns = router.urls

# urlpatterns = [
#     path('clientes/', views.ClienteListar.as_view()),
#     path('usuarios/', views.UsuarioListar.as_view()),
#     path('clientes/<int:pk>/', views.ClienteDetalhes.as_view()),
#     path('fotos/', views.FotoListar.as_view()),
#     path('fotos/<int:pk>', views.FotoDetalhes.as_view()),
#     path('fotosIn/', views.FotoInListar.as_view()),
# ]

 