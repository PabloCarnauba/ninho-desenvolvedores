# soma dos números pares entre 1 e 100
soma = 0

for i in range(101):
    if (i % 2)==0:
        print(i)
        soma += i
        
print("A soma dos números é:", soma)

# média dos numeros pares entre 1 e 1000
soma = 0
qtdpares = 0
for i in range(1,1000):
    if (i % 2)==0:
        print(i)
        soma += i
        qtdpares += 1

print(f"A média dos números é:", soma/qtdpares)