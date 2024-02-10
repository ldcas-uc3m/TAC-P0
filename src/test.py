from time import perf_counter
import random

import matplotlib.pyplot as plt
import pandas as pd

import gcdlib
import primeslib



ITERATIONS = 420
IMAGES_OUTPUT_FOLDER = "report/img"
CSV_OUTPUT_FOLDER = "data"


def funct_tests() -> pd.DataFrame:
    """
    Tests the performance of functions.

    :return:
    """

    df = pd.DataFrame(columns = ['n', 'time', 'order','result'])

    counter = 0

    while counter < 21:

        tic = perf_counter()
        resultado_actual = primeslib.is_prime(counter)
        toc = perf_counter()

        results = pd.Series(
            {
                'n': counter,
                'time': toc - tic,
                'order': len(str(counter)),
                'result': resultado_actual
            }
        )
        df.loc[len(df)] = results
        counter += 1

    return df
    



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

            results = pd.Series(
                {
                    'n': n,
                    'time': toc - tic,
                    'order': len(str(maxN)),
                    'result': resultado_actual
                }
            )

            # update df
            df.loc[len(df)] = results

            counter+=1

        # update N
        minN = maxN
        maxN = maxN*10

        print(f"Iteración {len(str(maxN))}: {n}")
        print(f"Tiempo de ejecución: {toc - tic} segundos\n")


    return df.sort_values(by='n', ignore_index=True)




def plot_performance(numeros, tiempos, filename: str, title: str, xlabel: str, ylabel: str):
    
    plt.figure(figsize=(6, 4))

    # Crear un gráfico de dispersión
    plt.plot(numeros, tiempos, marker='o', color='blue', linestyle='-')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    # Mostrar el gráfico
    plt.savefig(f'{IMAGES_OUTPUT_FOLDER}/{filename}.png')




if __name__ == "__main__":

    results_df = perf_tests()

    #funct_df = funct_tests()

    results_df.to_csv(f'{CSV_OUTPUT_FOLDER}/output_primes.csv')

    #funct_df.to_csv(f'{CSV_OUTPUT_FOLDER}/output_primes_fucnt_test.csv')


    #results_df = pd.read_csv(f'{CSV_OUTPUT_FOLDER}/output_primes.csv')

    avg = results_df.groupby('order')['time'].mean()  # average per order

    plot_performance(
        avg.index,
        avg.values,
        filename='scatter_plot_primes',
        title='Relación entre Longitud del Número y Tiempo de Ejecución',
        xlabel='Longitud del Número',
        ylabel='Tiempo de Ejecución (segundos)'
    )

    primes = results_df.loc[results_df['result'] == True]  # only true values
    plot_performance(
        primes['n'],
        primes['time'],
        filename='scatter_plot_primes_only_primes',
        title='Relación entre números primos y Tiempo de Ejecución',
        xlabel='n',
        ylabel='Tiempo de Ejecución (segundos)'
    )



