from time import perf_counter
import random
from typing import Callable

import matplotlib.pyplot as plt
from numpy.typing import ArrayLike
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
    



def perf_tests(fn: Callable, max: int | float, nargs: int = 1, iterations: int = ITERATIONS) -> pd.DataFrame:
    """
    Tests the performance of functions, giving them random int arguments (with the same number of digits) up to `max`.

    :param fn: Function to test.
    :param max: Maximum allowed number for the tests to be performed.
    :param nargs: Number of arguments of `fn`.
    :param iterations: Number of iterations per digit.

    :return: DataFrame with colums {'a': arg a, ..., 'time': time it took to compute, 'order': number of digits, 'result': result}
    """

    columns = [ chr(ord('a') + i) for i in range(nargs) ]  # one column per argument: ['a', 'b', ...]
    columns.extend(['time', 'order','result'])

    df = pd.DataFrame(columns = columns)

    ranges = [(10**i, 10**(i+1) - 1) for i in range(len(str(int(max))) - 1)]  # [(1, 99), (10, 999), ...]

    for minN, maxN in ranges:
        print(f"Iteración {len(str(maxN))}:", end=' ', flush=True)
        start = perf_counter()

        for _ in range(iterations):

            # generate random args
            args = [ random.randint(minN, maxN) for _ in range(nargs) ]

            # execute
            tic = perf_counter()
            resultado_actual = fn(*args)
            toc = perf_counter()

            # write results
            results_dict = {  # {'a': args[0], ...}
                columns[i]: args[i]
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

        stop = perf_counter()
        print(f"{stop - start} s")


    return df




def plot_performance(numeros: ArrayLike, tiempos: ArrayLike, filename: str, title: str, xlabel: str, ylabel: str):
    """
    Plots the performance of a function in a matplotlib graph, and saves it to `IMAGES_OUTPUT_FOLDER/filename`.

    :param numeros: Size of problem (n).
    :param tiempos: Time it took (s).
    :param filename: Name of the file to store.
    :param xlabel: Label of X axis (size of problem).
    :param ylabel: Label of Y axis (time).
    """

    plt.figure(figsize=(6, 4))

    # Crear un gráfico de dispersión
    plt.plot(numeros, tiempos, marker='o', color='blue', linestyle='-')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    # Fix the X axis
    plt.xticks(range(1, len(numeros)+1), [str(n) for n in numeros])

    # Guardar el gráfico
    plt.savefig(f'{IMAGES_OUTPUT_FOLDER}/{filename}.png')




if __name__ == "__main__":

    # PRIMES

    print("\n--- Testing primeslib.is_prime ---\n")
    results_df = perf_tests(primeslib.is_prime, primeslib.MAX_UINT).sort_values(by='a', ignore_index=True).rename(columns={'a': 'n'})

    funct_df = funct_tests()

    results_df.to_csv(f'{CSV_OUTPUT_FOLDER}/output_primes.csv')
    funct_df.to_csv(f'{CSV_OUTPUT_FOLDER}/output_primes_fucnt_test.csv')

    # results_df = pd.read_csv(f'{CSV_OUTPUT_FOLDER}/output_primes.csv')

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
    avgprimes = primes.groupby('order')['time'].mean()  # average per order

    plot_performance(
        avgprimes.index,
        avgprimes.values,
        filename='scatter_plot_primes_only_primes',
        title='Relación entre números primos y Tiempo de Ejecución',
        xlabel='Longitud del Número',
        ylabel='Tiempo de Ejecución (segundos)'
    )


    # GCD

    for fn, name, iterations, max in [
            (
                gcdlib.gcd_euclid,
                'euclid',
                ITERATIONS,
                gcdlib.MAX_INT
            ),
            (
                gcdlib.gcd_factorize,
                'factorize',
                5,
                10e10  # 11 digits
            )
        ]:

        print(f"\n--- Testing gcdlib.gcd_{name} ---\n")

        results_df = perf_tests(fn, max, iterations=iterations, nargs=2)

        results_df.to_csv(f'{CSV_OUTPUT_FOLDER}/output_gcd_{name}.csv')
        # results_df = pd.read_csv(f'{CSV_OUTPUT_FOLDER}/output_gcd_{name}.csv')

        # Transform into int to represent the number of digits without zeroes 1.0 -> 1
        results_df['order'] = results_df['order'].astype(int)
        avg = results_df.groupby('order')['time'].mean()  # average per order

        plot_performance(
            avg.index,
            avg.values,
            filename=f'scatter_plot_gcd_{name}',
            title='Relación entre Longitud del Número y Tiempo de Ejecución',
            xlabel='Longitud del Número',
            ylabel='Tiempo de Ejecución (segundos)'
        )


