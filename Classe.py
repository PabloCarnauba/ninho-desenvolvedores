'''
class Pessoa:
    def __init__(self, nome, sexo, cpf, ativo):
        self.nome = nome
        self.sexo = sexo
        self.cpf = cpf
        self.ativo = ativo
        
    def desativar(self):
        self.ativo = False
        print("A pessooa foi desativada com sucesso")
        
if __name__ == "__main__":
    pessoa1 = Pessoa("João", "M", "123456", True)
    pessoa1.desativar()
'''

# Crie uma classe que representa um carro. Os atributos dele serão Modelo, Ano, Placa, Fabricante, Velocidade.
# Crie um método acelerar que aumentar a velocidade do carro.
# Crie um método parar que zera a velocidade do carro
# Crie um método ver_informacoes que imprime as informações do carro e informa se ele está parado ou em movimento.
# No arquivo main.py crie 3 carros diferentes, acelere eles para velocidades diferentes e exiba suas informações na tela. Lembrar de dar import.

class Carro:
    def __init__(self, ano, placa, fabricante, velocidade):
        self.ano = ano
        self.placa = placa
        self.fabricante = fabricante
        self.velocidade = velocidade
        
    def speed(self):
        self.velocidade = self.velocidade +100
        print(f"\nCarro {self.fabricante} em burst...")
        print(f"Sua velocidade é: {self.velocidade}km/h")
        
    def slow(self):
        self.velocidade = 0
        print(f"\nCarro {self.fabricante} está no modo slow... freando...")
        print(f"Sua velocidade é: {self.velocidade}km/h")
   
    def informações(self):
        print(f'''
    Fabricante: {self.fabricante}          
    Ano: {self.ano}
    Placa: {self.placa}
    Velocidade Atual: {self.velocidade}km/h 
              ''')

        if self.velocidade >0:
            print("Status: Em movimento")
        else:
            print("Status: Parado")