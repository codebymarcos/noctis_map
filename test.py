# calculadora
def calculadora():
    print("=== Calculadora Simples ===")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    
    opcao = input("\nEscolha uma operação (1-4): ")
    
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    
    if opcao == '1':
        resultado = num1 + num2
        print(f"\n{num1} + {num2} = {resultado}")
    elif opcao == '2':
        resultado = num1 - num2
        print(f"\n{num1} - {num2} = {resultado}")
    elif opcao == '3':
        resultado = num1 * num2
        print(f"\n{num1} × {num2} = {resultado}")
    elif opcao == '4':
        if num2 != 0:
            resultado = num1 / num2
            print(f"\n{num1} ÷ {num2} = {resultado}")
        else:
            print("\nErro: Divisão por zero!")
    else:
        print("\nOpção inválida!")

if __name__ == "__main__":
    calculadora()