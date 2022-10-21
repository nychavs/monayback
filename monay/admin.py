from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Cliente)
admin.site.register(models.Usuario)
admin.site.register(models.Emprestimo)
admin.site.register(models.PgtoEmprestimo)
admin.site.register(models.Endereco)
admin.site.register(models.Contato)
admin.site.register(models.Conta)
admin.site.register(models.Favorito)
admin.site.register(models.Extrato)
admin.site.register(models.Transacao)
admin.site.register(models.Cartao)
admin.site.register(models.Fatura)