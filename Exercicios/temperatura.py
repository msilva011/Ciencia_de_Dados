import numpy as np

temperaturas = np.array([2.5, 3.2, 5.1, 6.3, 7.0, 8.1, 10.5, 9.8, 8.5, 7.3,
    6.2, 5.1, 4.5, 3.8, 5.6, 6.7, 7.2, 8.3, 10.1, 9.4,
    8.2, 7.0, 6.3, 5.4, 4.7, 3.9, 5.8, 6.9, 7.4, 8.5,
    10.3, 9.6, 8.4, 7.2, 6.5, 5.6, 4.9, 4.1, 5.9, 7.0,
    7.5, 8.6, 10.4, 9.7, 8.5, 7.3, 6.6, 5.7, 5.0, 4.2,
    6.0, 7.1, 7.6, 8.7, 10.6, 9.9, 8.7, 7.5, 6.8, 5.9,
    5.2, 4.4, 6.1, 7.2, 7.7, 8.8, 10.7, 10.0, 8.8, 7.6,
    6.9, 6.0, 5.3, 4.5, 6.2, 7.3, 7.8, 8.9, 10.8, 10.2,
    9.0, 7.8, 7.1, 6.2, 5.5, 4.7, 6.3, 7.4, 7.9, 9.0,
    10.9, 10.3, 9.1, 7.9, 7.2, 6.3, 5.6, 4.8, 6.4, 7.5])

media = round(np.mean(temperaturas),2)

mediana = round(np.median(temperaturas),2)

desvio_padrao = round(np.std(temperaturas),2)

print("***************************")
print("Media:", media, "\nMediana:", mediana, "\nDesvio Padrao:", desvio_padrao)
print("***************************")

limite_frio = 5
limite_quente = 15

def classificar_temperatura(temp):
    if temp < limite_frio:
        return "Frio"
    elif temp < limite_quente:
        return "Moderado"
    else:
        return "Quente"

categorias = np.array([classificar_temperatura(temp) for temp in temperaturas])

print("Categorias de Temperatura:")
for i in range(len(temperaturas)):
    print(f"{temperaturas[i]} graus: {categorias[i]}")

indice_dia_mais_frio = np.argmin(temperaturas)
temperatura_dia_mais_frio = temperaturas[indice_dia_mais_frio]

indice_dia_mais_quente = np.argmax(temperaturas)
temperatura_dia_mais_quente = temperaturas[indice_dia_mais_quente]

print("***************************")
print("Dia mais frio:", temperatura_dia_mais_frio, "graus")
print("Dia mais quente:", temperatura_dia_mais_quente, "graus")
print("***************************")

