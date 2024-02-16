from time import perf_counter
import random
from typing import Callable

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
    



def perf_tests(fn: Callable, max: int, nargs: int = 1, iterations: int = ITERATIONS) -> pd.DataFrame:
    """
    Tests the performance of functions, giving them random int arguments up to `max`.

    :param fn: function to test
    :param nargs: number of arguments of the function.
    :param iterations: number of iterations per digit.

    :return: DataFrame with colums {'a': arg a, ..., 'time': time it took to compute, 'order': number of digits, 'result': result}
    """

    columns = [ chr(ord('a') + i) for i in range(nargs) ]
    columns.extend(['time', 'order','result'])

    df = pd.DataFrame(columns = columns)

    minN = 0
    maxN = 9

    while maxN < max:
        counter = 0

        while counter < iterations:
            args = [ random.randint(minN, maxN) for _ in range(nargs) ]

            tic = perf_counter()
            resultado_actual = fn(*args)
            toc = perf_counter()

            results_dict = {  # {'a': args[0], ...}
                chr(ord('a') + i): args[i]
                for i in range(nargs)
            }

            results_dict.update(
                {
                    'time': toc - tic,
                    'order': len(str(maxN)),
                    'result': resultado_actual
                }
            )
            results = pd.Series(results_dict)

            # update df
            df.loc[len(df)] = results

            counter+=1

        # update N
        minN = maxN
        maxN = maxN*10

        print(f"Iteración {len(str(maxN))}: {args}")
        print(f"Tiempo de ejecución: {toc - tic} segundos\n")


    return df




def plot_performance(numeros, tiempos, filename: str, title: str, xlabel: str, ylabel: str):
    
    plt.figure(figsize=(6, 4))

    # Crear un gráfico de dispersión
    plt.plot(numeros, tiempos, marker='o', color='blue', linestyle='-')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    plt.xticks(range(int(min(numeros)), int(max(numeros))+1))
    plt.yticks(range(int(min(tiempos)), int(max(tiempos))+1))

    # Mostrar el gráfico
    plt.savefig(f'{IMAGES_OUTPUT_FOLDER}/{filename}.png')




if __name__ == "__main__":

    # PRIMES

    # results_df = perf_tests(primeslib.is_prime, primeslib.MAX_UINT).sort_values(by='a', ignore_index=True).rename(columns={'a': 'n'})

    # funct_df = funct_tests()

    # results_df.to_csv(f'{CSV_OUTPUT_FOLDER}/output_primes.csv')

    # funct_df.to_csv(f'{CSV_OUTPUT_FOLDER}/output_primes_fucnt_test.csv')


    # results_df = pd.read_csv(f'{CSV_OUTPUT_FOLDER}/output_primes.csv')

    # avg = results_df.groupby('order')['time'].mean()  # average per order

    # plot_performance(
    #     avg.index,
    #     avg.values,
    #     filename='scatter_plot_primes',
    #     title='Relación entre Longitud del Número y Tiempo de Ejecución',
    #     xlabel='Longitud del Número',
    #     ylabel='Tiempo de Ejecución (segundos)'
    # )

    # primes = results_df.loc[results_df['result'] == True]  # only true values
    # plot_performance(
    #     primes['n'],
    #     primes['time'],
    #     filename='scatter_plot_primes_only_primes',
    #     title='Relación entre números primos y Tiempo de Ejecución',
    #     xlabel='n',
    #     ylabel='Tiempo de Ejecución (segundos)'
    # )


    # GCD

    
    results_df = perf_tests(gcdlib.gcd_factorize, 10e8, nargs=2, iterations=50).sort_values(by='a', ignore_index=True)

    avg = results_df.groupby('order')['time'].mean()  # average per order
    plot_performance(
        avg.index,
        avg.values,
        filename='scatter_plot_gcd',
        title='Relación entre Longitud del Número y Tiempo de Ejecución',
        xlabel='Longitud del Número',
        ylabel='Tiempo de Ejecución (segundos)'
    )


