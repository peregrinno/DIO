class Heroi:
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo

    def atacar(self):
        if self.tipo == "mago":
            ataque = "magia"
        elif self.tipo == "guerreiro":
            ataque = "espada"
        elif self.tipo == "monge":
            ataque = "artes marciais"
        elif self.tipo == "ninja":
            ataque = "shuriken"
        else:
            ataque = "ataque desconhecido"
        
        print(f"O {self.tipo} atacou usando {ataque}")

# Criando instâncias dos heróis
heroi1 = Heroi("Arthur", 30, "guerreiro")
heroi2 = Heroi("Merlin", 150, "mago")
heroi3 = Heroi("Shaolin", 25, "monge")
heroi4 = Heroi("Hanzo", 28, "ninja")

# Heróis atacando
heroi1.atacar()
heroi2.atacar()
heroi3.atacar()
heroi4.atacar()
