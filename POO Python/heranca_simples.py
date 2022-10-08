class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print("ligando o motor")


class Motocicleta(Veiculo):
    pass


class Carro(Veiculo):
    pass


class Caminhao(Veiculo):
    def __init__(self, cor, placa, numero_rodas, carregado):
        super().__init__(cor, placa, numero_rodas, carregado) #apesar de ter outro construtor eu chamo a implementação doq eu preciso da classe mae
        self.carregado = carregado
    def esta_carregado(self):
        if not(self.carregado):
            print("Não estou carregado")
        else:
            print("Estou carregado")


moto = Motocicleta("preta", "qwer-123", 2)
print(moto)
moto.ligar_motor()


caminhao = Caminhao("vermelho", "qrwh-256", 8)
print(caminhao)
caminhao.ligar_motor()
caminhao.esta_carregado()


carro = Carro("prata", "poiu-987", 4)
print(carro)
carro.ligar_motor()
