import Classe

carro1 = Classe.Carro("2005", 243, "BMW", 10)
carro2 = Classe.Carro("2010", 256, "Ferrari", 50)
carro3 = Classe.Carro("2015", 687, "Corola", 20)

carro1.speed()
carro2.speed()
carro3.slow()

lista = [carro1, carro2, carro3]

for i in range(len(lista)):
    print("")
    lista[i].informações()