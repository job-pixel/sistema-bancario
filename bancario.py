# Lista de contas bancárias
contas = []
numero_conta = 1

# Função para exibir o menu
def menu():
    print("\nBem-vindo ao Sistema Bancário!")
    print("1 - Criar Conta")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Extrato")
    print("5 - Sair")
    
    opcao = input("Escolha uma opção: ")
    return opcao

# Função para criar uma conta
def criar_conta():
    global numero_conta
    
    print("\n=== Criar Nova Conta ===")
    nome = input("Nome do Titular: ")
    cpf = input("CPF (apenas números): ")
    
    for conta in contas:
        if conta["cpf"] == cpf:
            print("Erro: CPF já cadastrado!")
            return
    
    nova_conta = {
        "numero": numero_conta,
        "titular": nome,
        "cpf": cpf,
        "saldo": 0.0
    }
    
    contas.append(nova_conta)
    print(f"Conta criada com sucesso! Número da conta: {numero_conta}")
    numero_conta += 1

# Função para depositar dinheiro em uma conta
def depositar():
    numero_conta = int(input("\nDigite o número da conta: "))
    valor = float(input("Digite o valor do depósito: "))
    
    conta = next((conta for conta in contas if conta["numero"] == numero_conta), None)
    
    if conta:
        conta["saldo"] += valor
        print(f"Depósito de R${valor:.2f} realizado com sucesso na conta {numero_conta}. Novo saldo: R${conta['saldo']:.2f}")
    else:
        print("Conta não encontrada!")

# Função para sacar dinheiro de uma conta
def sacar():
    numero_conta = int(input("\nDigite o número da conta: "))
    valor = float(input("Digite o valor do saque: "))
    
    conta = next((conta for conta in contas if conta["numero"] == numero_conta), None)
    
    if conta:
        if conta["saldo"] >= valor:
            conta["saldo"] -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso na conta {numero_conta}. Novo saldo: R${conta['saldo']:.2f}")
        else:
            print("Saldo insuficiente!")
    else:
        print("Conta não encontrada!")

# Função para ver o extrato de uma conta
def extrato():
    numero_conta = int(input("\nDigite o número da conta: "))
    
    conta = next((conta for conta in contas if conta["numero"] == numero_conta), None)
    
    if conta:
        print(f"Extrato da conta {numero_conta}:")
        print(f"Saldo atual: R${conta['saldo']:.2f}")
    else:
        print("Conta não encontrada!")

# Função principal para rodar o sistema
def main():
    while True:
        opcao = menu()
        
        if opcao == "1":
            criar_conta()
        elif opcao == "2":
            depositar()
        elif opcao == "3":
            sacar()
        elif opcao == "4":
            extrato()
        elif opcao == "5":
            print("Saindo do sistema. Obrigado!")
            break
        else:
            print("Opção inválida. Tente novamente!")

# Chama a função principal para iniciar o programa
if __name__ == "__main__":
    main()