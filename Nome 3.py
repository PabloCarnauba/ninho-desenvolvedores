def revisao1():
    nomes = ""
    
    for i in range(5):
        
        nome = input("Digite um nome:\n")
        
        nomes += f"{i+1}. {nome} \n" 
              
    print(nomes)

revisao1()