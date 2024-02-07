from time import perf_counter
import random

import matplotlib.pyplot as plt
from statistics import mean
import csv

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

        counter = 0
        avgTime = []

        #For it length of number calculates it 10 times and get the mean value for calculation time
        while counter <= 9:
            inicio_tiempo = perf_counter()
            resultado_actual = gcdlib.gcd_factorize(a, b)
            fin_tiempo = perf_counter()
            avgTime.append(fin_tiempo - inicio_tiempo)
            counter+=1

        numeros.append(len(str(maxN)))
        tiempos.append(mean(avgTime))

        print(f"Iteración: MCD({a}, {b}) = {resultado_actual}")
        print(f"Tiempo de ejecución: {fin_tiempo - inicio_tiempo} segundos\n")

        minN = maxN
        maxN = maxN*10

        a = random.randint(minN, maxN)
        b = random.randint(minN, maxN)

    return numeros, tiempos


#The data obtained for time consumption to calculate number of different number of digits
def plot_performance(numeros, tiempos):
    
    plt.figure(figsize=(6, 4))

    # Crear gráfico
    plt.plot(numeros, tiempos, marker='o', color='blue', linestyle='-')
    plt.title('Relación entre Longitud del Número y Tiempo de Ejecución')
    plt.xlabel('Longitud del Número')
    plt.ylabel('Tiempo de Ejecución (segundos)')

    # Mostrar el gráfico
    plt.savefig('scatter_plot.png')



def saveCSV(numbers, times):

    data = zip(numbers, times)

    # Write to CSV file
    with open('output.csv', 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Digits', 'Time'])  
        csv_writer.writerows(data)  



perf_results, perf_times = calc_performance()

# Función para generar el grafico a aprtir de los datos calculados
plot_performance(perf_results, perf_times)

saveCSV(perf_results, perf_times)


print("Resultados:", perf_results)
print("Tiempos:", perf_times)