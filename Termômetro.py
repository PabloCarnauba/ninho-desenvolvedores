temp = float(input("Digite a temperatura em graus Celsius:"))

if temp >= 0 and temp < 37.3:
    print("Você não está com febre! :)")
elif temp >= 37.3 and temp <= 37.7:
    print("Você está febrículo! :/")
elif temp >= 38.8 and temp < 39.0:
    print("Você está com febre! :(")
elif temp > 39.0:
    print("Você está com febre alta! ;_;")
else:
    print("Digite um valor válido!")