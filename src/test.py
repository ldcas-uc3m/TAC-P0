import sys 
from time import perf_counter
import random
import csv
from statistics import mean

import matplotlib.pyplot as plt
import pandas as pd

import gcdlib
import primeslib




ITERATIONS = 69



def perf_tests() -> pd.DataFrame:
    """
    Tests the performance of functions.

    :return:
    """

    df = pd.DataFrame(columns = ['n', 'time', 'order','result'])

    minN = 0
    maxN = 9

    while maxN < primeslib.MAX_UINT:
        counter = 0

        while counter < ITERATIONS:
            n = random.randint(minN, maxN)
            tic = perf_counter()
            resultado_actual = primeslib.is_prime(n)
            toc = perf_counter()

            df.append(
                {
                    'n': n,
                    'time': toc - tic,
                    'order': len(str(maxN)),
                    'result': resultado_actual
                }
            )

            counter+=1

        # update N
        minN = maxN
        maxN = maxN*10

        print(f"Iteración {len(str(maxN))}: {n}")
        print(f"Tiempo de ejecución: {toc - tic} segundos\n")


    return df


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
        plt.savefig('report/img/scatter_plot_gcd.png')
    else:
        plt.savefig('report/img/scatter_plot_primes.png')


def save_csv(numbers, times, filename='data/output_gcd.csv'):

    data = zip(numbers, times)
    # Write to CSV file
    with open(filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Number', 'Time'])  # Write header
        csv_writer.writerows(data)  # Write data


def save_csv2(numbers, times, filename='data/output_primes.csv'):

    data = zip(numbers, times)
    # Write to CSV file
    with open(filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Number', 'Time'])  # Write header
        csv_writer.writerows(data)  # Write data



if __name__ == "__main__":

    results_df = perf_tests()

    #perf_results_gcd, perf_times_gcd = calc_performance()


    # Crear gráfico de dispersión
    #plot_performance(perf_results_gcd, perf_times_gcd, 'gcd')
    plot_performance(perf_results_primes, perf_times_primes, 'primes')

    #save_csv(perf_results_gcd, perf_times_gcd)
    save_csv2(perf_results_primes, perf_times_primes)



