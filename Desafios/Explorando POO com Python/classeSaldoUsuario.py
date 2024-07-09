class PlanoTelefone:
    def __init__(self, nome, saldo):
        self._nome = nome
        self._saldo = saldo

    @property
    def nome(self):
        return self._nome

    @property
    def saldo(self):
        return self._saldo

    def verificar_saldo(self):
        return self._saldo

    def mensagem_personalizada(self):
        if self._saldo < 10:
            return "Seu saldo está baixo. Recarregue e use os serviços do seu plano."
        elif self._saldo >= 50:
            return "Parabéns! Continue aproveitando seu plano sem preocupações."
        else:
            return "Seu saldo está razoável. Aproveite o uso moderado do seu plano."

class UsuarioTelefone:
    def __init__(self, nome, plano):
        self._nome = nome
        self._plano = plano

    def verificar_saldo(self):
        saldo = self._plano.verificar_saldo()
        mensagem = self._plano.mensagem_personalizada()
        return saldo, mensagem

usuarios_dados = [
    ("João", "Essencial", 9),
    ("Debora", "Prata", 11),
    ("Catarina", "Premium", 50)
]

for nome, plano, saldo in usuarios_dados:
    plano_usuario = PlanoTelefone(plano, saldo)
    usuario = UsuarioTelefone(nome, plano_usuario)
    saldo_usuario, mensagem_usuario = usuario.verificar_saldo()
    print(f"{nome} ({plano}): {mensagem_usuario}")
