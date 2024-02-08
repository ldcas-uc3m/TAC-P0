from time import perf_counter
import random

import matplotlib.pyplot as plt

import gcdlib
import primeslib

import csv

import sys 

from statistics import mean

#print(primeslib.MAX_UINT)
#print(gcdlib.gcd_factorize(24, 36))



def primes_perf():

    numeros = []
    tiempos = []

    minN = 0
    maxN = 9

    n = random.randint(minN, maxN)

    while maxN < sys.maxsize:
        counter = 0
        times = []

        while counter < 9:
            inicio_tiempo = perf_counter()
            resultado_actual = primeslib.is_prime(n)
            fin_tiempo = perf_counter()
            times.append(fin_tiempo - inicio_tiempo)
            counter+=1

        numeros.append(len(str(maxN)))
        tiempos.append(mean(times))

        minN = maxN
        maxN = maxN*10

        print(f"Iteración: IsPrime({n}) = {resultado_actual}")
        print(f"Tiempo de ejecución: {fin_tiempo - inicio_tiempo} segundos\n")

        n = random.randint(minN, maxN)

    return numeros, tiempos


def calc_performance():
   
    numeros = []
    tiempos = []

    minN = 0
    maxN = 10
    a = random.randint(minN, maxN)
    b = random.randint(minN, maxN)


    while maxN < sys.maxsize:
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



def plot_performance(numeros, tiempos, function):
    
    plt.figure(figsize=(6, 4))

    # Crear un gráfico de dispersión
    plt.plot(numeros, tiempos, marker='o', color='blue', linestyle='-')
    plt.title('Relación entre Longitud del Número y Tiempo de Ejecución')
    plt.xlabel('Longitud del Número')
    plt.ylabel('Tiempo de Ejecución (segundos)')

    # Mostrar el gráfico
    if function == 'gcd':
        plt.savefig('scatter_plot_gcd.png')
    else:
        plt.savefig('scatter_plot_primes.png')


def save_csv(numbers, times, filename='output_gcd.csv'):

    data = zip(numbers, times)
    # Write to CSV file
    with open(filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Number', 'Time'])  # Write header
        csv_writer.writerows(data)  # Write data


def save_csv2(numbers, times, filename='output_primes.csv'):

    data = zip(numbers, times)
    # Write to CSV file
    with open(filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Number', 'Time'])  # Write header
        csv_writer.writerows(data)  # Write data



perf_results_primes, perf_times_primes = primes_perf()

#perf_results_gcd, perf_times_gcd = calc_performance()


# Crear gráfico de dispersión
#plot_performance(perf_results_gcd, perf_times_gcd, 'gcd')
plot_performance(perf_results_primes, perf_times_primes, 'primes')

#save_csv(perf_results_gcd, perf_times_gcd)
save_csv2(perf_results_primes, perf_times_primes)



