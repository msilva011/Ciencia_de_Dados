def conver(valor, unidade_inicial, unidade_final):
  
    if unidade_inicial == "pe" and unidade_final == "metro":
        return valor * 0.3048
    elif unidade_inicial == "metro" and unidade_final == "pe":
        return valor * 3.281
    elif unidade_inicial == "jarda" and unidade_final == "metro":
        return valor * 0.9144
    elif unidade_inicial == "jarda" and unidade_final == "pe":
        return valor * 3.0

unidade_inicial = input("Digite a unidade origem (pe, metro, jarda): ")
valor = float(input("Digite o valor: "))
unidade_final = input("Digite a unidade destino (pe, metro, jarda): ")

resultado = conver(valor, unidade_inicial, unidade_final)
print(f"Saída: {resultado:.4f}")