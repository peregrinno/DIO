class UsuarioTelefone:
    def __init__(self, nome, numero, plano):
        self._nome = nome
        self._numero = numero
        self._plano = plano

    @property
    def nome(self):
        return self._nome

    @property
    def numero(self):
        return self._numero

    @property
    def plano(self):
        return self._plano

    def __str__(self):
        return f"Usuário {self._nome} criado com sucesso."

# Simulação dos dados de entrada:
usuarios_dados = [
    ("Ana", "(11) 91111-1111", "Plano Essencial Fibra"),
    ("Sofia", "(22) 92222-2222", "Plano Prata Fibra"),
    ("Pedro", "(33) 93333-3333", "Plano Premium Fibra")
]

# Criação dos objetos UsuarioTelefone e impressão da mensagem de sucesso:
usuarios = [UsuarioTelefone(nome, numero, plano) for nome, numero, plano in usuarios_dados]

for usuario in usuarios:
    print(usuario)
