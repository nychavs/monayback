from django.db import models
from pictures.models import PictureField
# Create your models here.

class Emprestimo(models.Model):
    EMPREST_AUTORIZADO = 'A'
    EMPREST_NEGADO = 'N'

    STATUS_EMPREST = [
        (EMPREST_AUTORIZADO, 'Autorizado'),
        (EMPREST_NEGADO, 'Negado'),
    ]
    statusEmprest = models.CharField(max_length=1, choices=STATUS_EMPREST, default=EMPREST_NEGADO)
    dataEmprest = models.DateField() 
    valorEmprest = models.DecimalField(max_digits=10, decimal_places=2)
    qtdParcelas = models.PositiveSmallIntegerField()
    jurosEmprest = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.valorEmprest)

class PgtoEmprestimo(models.Model):
    valorPgto = models.DecimalField(max_digits=10, decimal_places=2)
    dataPgto = models.DateField()
    dataVenc = models.DateField()
    emprestimo = models.ForeignKey(Emprestimo, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.emprestimo)

class Usuario(models.Model):
    # autenticar
    cpfUsuario = models.CharField(max_length=14)
    senhaUsuario = models.CharField(max_length=15)
    statusUsuario = models.BooleanField()
    def __str__(self):
        return str(self.cpfUsuario)

class Cliente(models.Model):
    FEMININO = 'F'
    MASCULINO = 'M'
    NAO_INFORMAR = 'N'

    GENERO = [
        (FEMININO, 'Feminino'),
        (MASCULINO, 'Masculino'),
        (NAO_INFORMAR, 'Nao informado'),
    ]

    nomeCliente = models.CharField(max_length=50)
    dataNascimento = models.DateField()
    genero = models.CharField(max_length=1, choices=GENERO, default=NAO_INFORMAR)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fotoCliente = PictureField(upload_to='loja/imagens')

    def __str__(self):
        return str(self.nomeCliente)

class Endereco(models.Model):
    numero = models.CharField(max_length=5)
    rua = models.CharField(max_length=15)
    bairro = models.CharField(max_length=15)
    cidade = models.CharField(max_length=15)
    estado = models.CharField(max_length=2)
    cep = models.CharField(max_length=9)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.cliente)

class Contato(models.Model):
    telefoneCliente = models.CharField(max_length=11)
    emailCliente = models.CharField(max_length=50)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.cliente)

class Conta(models.Model):
    CONTA_POUPANCA = 'P'
    CONTA_CORRENTE = 'C'
    CONTA_SALARIO ='S'

    TIPO_CONTA = [
        (CONTA_POUPANCA, 'Poupanca'),
        (CONTA_CORRENTE, 'Corrente'),
        (CONTA_SALARIO, 'Salario'),
    ]
    agencia = models.CharField(max_length=4)
    numeroConta = models.CharField(max_length=7)
    tipoConta = models.CharField(max_length=1, choices=TIPO_CONTA, default=CONTA_CORRENTE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    saldoConta = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.numeroConta)

class Favorito(models.Model):
    CHAVE_CPF_CNPJ = 'C'
    CHAVE_EMAIL = 'E'
    CHAVE_TELEFONE = 'T'

    CHAVE_TRANSF = [
        (CHAVE_CPF_CNPJ, 'CPF/CNPJ'),
        (CHAVE_EMAIL, 'Email'),
        (CHAVE_TELEFONE, 'Telefone'),
    ]
    nomeContato = models.CharField(max_length=50)
    chaveTipo = models.CharField(max_length= 1, choices=CHAVE_TRANSF, default=CHAVE_TELEFONE)
    chaveValor = models.CharField(max_length=50)
    contaDestinatario = models.ForeignKey(Conta, on_delete=models.CASCADE, related_name='contaDestinatario')
    contaRemetente = models.ForeignKey(Conta, on_delete=models.CASCADE, related_name='contaRemetente')

    def __str__(self):
        return str(self.nomeContato)

class Extrato(models.Model):
    contaExtrato = models.ForeignKey(Conta, on_delete=models.CASCADE)
    valorExtrato = models.DecimalField(max_digits=10, decimal_places=2)
    tipoExtrato = models.CharField(max_length=20)
    dataExtrato = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.valorExtrato)

class Transacao(models.Model):
    valorTransacao = models.DecimalField(max_digits=10, decimal_places=2)
    dataTransacao = models.DateTimeField(auto_now_add=True)
    destinatario = models.ForeignKey(Conta, on_delete=models.CASCADE, related_name='destinatario')
    remetente = models.ForeignKey(Conta, on_delete=models.CASCADE, related_name='remetente')

    def __str__(self):
        return str(self.destinatario)

class Cartao(models.Model):
    CARTAO_CREDITO = 'C'
    CARTAO_DEBITO = 'D'

    TIPO_CARTAO = [
        (CARTAO_CREDITO, 'Credito'),
        (CARTAO_DEBITO, 'Debito'),
    ]
    contaCliente = models.ForeignKey(Conta, on_delete=models.CASCADE)
    tipoCartao = models.CharField(max_length=1, choices=TIPO_CARTAO, default=CARTAO_DEBITO)
    limiteCartao = models.DecimalField(max_digits=10, decimal_places=2)
    numeroCartao = models.IntegerField()
    cvcCartao = models.CharField(max_length=4)
    nomeCartao = models.CharField(max_length=20)
    validadeCartao = models.CharField(max_length=5)
    diaVencFatura = models.PositiveSmallIntegerField()
    
    def __str__(self):
        return str(self.numeroCartao)

class Fatura(models.Model):
    dataVencimento = models.DateField()
    valorFatura = models.DecimalField(max_digits=10, decimal_places=2)
    dataPagamento = models.DateField()
    cartao = models.ForeignKey(Cartao, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.valorFatura)