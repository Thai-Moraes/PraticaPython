selecao = int(input("Você deseja usar que tipo de conversão hoje? \n1. Dólar --> Real \n2. Real --> Dólar\n"))
dolar_hoje = 4.78

if selecao == 1:
    dolar = float(input("Valor em Dólares: $"))
    print(f"Conversão para Reais (Dólar -> Real): R${dolar * dolar_hoje}")

if selecao == 2:
    real = float(input("Valor em Reais: R$"))
    print(f"Conversão para Dólares (Real -> Dólar): ${real / dolar_hoje}")