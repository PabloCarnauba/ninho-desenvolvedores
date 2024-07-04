def cadastroFuncionario():
    funcionarios = []

    while True:
        numeroMatricula = input("Digite o número de matrícula do funcionário (ou digite 'sair' para parar): ")
        if numeroMatricula == 'sair' or numeroMatricula == 'SAIR':
            break
        nome = input("Digite o nome do funcionário: ")
        cargo = input("Digite o cargo do funcionário: ")
        salario = float(input("Digite o salário do funcionário: "))

        funcionario = {"numeroMatricula": numeroMatricula, "nome": nome, "cargo": cargo, "salario": salario}
        funcionarios.append(funcionario)

    if funcionarios:
        salarioMax = funcionarios[0]
        salarioMin = funcionarios[0]

        for funcionario in funcionarios:
            if funcionario["salario"] > salarioMax["salario"]:
                salarioMax = funcionario
            if funcionario["salario"] < salarioMin["salario"]:
                salarioMin = funcionario

        print("\nFuncionário com maior salário:")
        print("Nome:", salarioMax["nome"])
        print("Salário: R$", salarioMax["salario"])

        print("\nFuncionário com menor salário:")
        print("Nome:", salarioMin["nome"])
        print("Salário: R$", salarioMin["salario"])

        print("\nOutros funcionários:")
        for funcionario in funcionarios:
            if funcionario != salarioMax and funcionario != salarioMin:
                print("\nMatrícula:", funcionario["numeroMatricula"])
                print("Nome:", funcionario["nome"])
                print("Cargo:", funcionario["cargo"])
                print("Salário: R$", funcionario["salario"])
    else:
        print("Nenhum funcionário cadastrado.")

    while True:
        print("\n----- Remoção de Funcionários -----")
        for funcionario in funcionarios:
            print(f'{funcionario["numeroMatricula"]} | {funcionario["nome"]} | {funcionario["cargo"]} | R$ {funcionario["salario"]}')
    
        matricula = input("Digite uma matrícula para remover um funcionário (0 para sair): ")
    
        if matricula == "0":
            break
    
        funcionarioEncontrado = None
        for funcionario in funcionarios:
            if funcionario["numeroMatricula"] == matricula:
                funcionarioEncontrado = funcionario
                break
        
        if funcionarioEncontrado:
            funcionarios.remove(funcionarioEncontrado)
            print(f"Funcionário com matrícula {matricula} removido com sucesso.")
        else:
            print("Matrícula inválida!")
            input("Pressione Enter para continuar.")

cadastroFuncionario()