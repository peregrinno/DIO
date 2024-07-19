class Plano:
    def __init__(self, saldo_inicial):
        self._saldo = saldo_inicial

    @property
    def saldo(self):
        return self._saldo

    def verificar_saldo(self):
        return self._saldo

    def custo_chamada(self, duracao):
        return 0.10 * duracao

    def deduzir_saldo(self, valor):
        if self._saldo >= valor:
            self._saldo -= valor
            return True
        else:
            return False

class UsuarioTelefone:
    def __init__(self, nome, numero, plano):
        self._nome = nome
        self._numero = numero
        self._plano = plano

    def fazer_chamada(self, destinatario, duracao):
        custo = self._plano.custo_chamada(duracao)
        if self._plano.deduzir_saldo(custo):
            return f"Chamada para {destinatario} realizada com sucesso. Saldo: ${self._plano.verificar_saldo():.2f}"
        else:
            return "Saldo insuficiente para fazer a chamada."

class UsuarioPrePago(UsuarioTelefone):
    def __init__(self, nome, numero, saldo_inicial):
        super().__init__(nome, numero, Plano(saldo_inicial))

usuarios_dados = [
    ("Rodrigo", "(00) 90000-0000", 10.00, "(33) 93333-3333", 60),
    ("Yule", "(11) 91111-1111", 30.00, "(00) 90000-0000", 240),
    ("Amelia", "(33) 93333-3333", 10.00, "(11) 91111-1111", 120)
]

for nome, numero, saldo, destinatario, duracao in usuarios_dados:
    usuario_pre_pago = UsuarioPrePago(nome, numero, saldo)
    print(usuario_pre_pago.fazer_chamada(destinatario, duracao))
