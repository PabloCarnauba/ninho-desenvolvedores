for i in range(2, 1000000):

    divisores = 0
    
    for j in range(1, i+1):
        
        if (i % j == 0):
            
            divisores += 1
            
    if divisores <= 2:
        print(i, "é primo")