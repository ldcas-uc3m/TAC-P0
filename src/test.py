from time import perf_counter
import random

import matplotlib.pyplot as plt

import gcdlib
import primeslib

print(primeslib.MAX_UINT)
print(primeslib.is_prime(17131175322357111317))

#print(gcdlib.gcd_factorize(24, 36))



def calc_performance():
   
    numeros = []
    tiempos = []

    minN = 0
    maxN = 10
    a = random.randint(minN, maxN)
    b = random.randint(minN, maxN)


    while maxN < 10000000000:
        inicio_tiempo = perf_counter()
        resultado_actual = gcdlib.gcd_factorize(a, b)
        fin_tiempo = perf_counter()

        numeros.append(len(str(maxN)))
        tiempos.append(fin_tiempo - inicio_tiempo)

        print(f"Iteración: MCD({a}, {b}) = {resultado_actual}")
        print(f"Tiempo de ejecución: {fin_tiempo - inicio_tiempo} segundos\n")

        minN = maxN
        maxN = maxN*10

        a = random.randint(minN, maxN)
        b = random.randint(minN, maxN)

    return numeros, tiempos



def plot_performance(numeros, tiempos):
    
    plt.figure(figsize=(6, 4))

    # Crear un gráfico de dispersión
    plt.plot(numeros, tiempos, marker='o', color='blue', linestyle='-')
    plt.title('Relación entre Longitud del Número y Tiempo de Ejecución')
    plt.xlabel('Longitud del Número')
    plt.ylabel('Tiempo de Ejecución (segundos)')

    # Mostrar el gráfico
    plt.savefig('scatter_plot.png')




perf_results, perf_times = calc_performance()


# Crear gráfico de dispersión
plot_performance(perf_results, perf_times)


print("Resultados:", perf_results)
print("Tiempos:", perf_times)