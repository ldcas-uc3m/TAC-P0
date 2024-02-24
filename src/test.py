from time import perf_counter
import random
from typing import Callable, Annotated, Iterable
import math

import matplotlib.pyplot as plt
import pandas as pd
from numpy.typing import ArrayLike

import gcdlib
import primeslib



ITERATIONS = 420
IMAGES_OUTPUT_FOLDER = "report/img"
CSV_OUTPUT_FOLDER = "data"


def func_test(fn: Callable, cases: Iterable) -> pd.DataFrame:
    """
    Tests the performance of a function given a set of cases.

    :param fn: Function to test.
    :param cases: Cases to test, passed as arguments to `fn`.

    :return: DataFrame with colums {n, time, order, result}
    """

    df = pd.DataFrame(columns = ['n', 'time', 'order','result'])

    for n in cases:

        tic = perf_counter()
        resultado_actual = fn(n)
        toc = perf_counter()


        results = pd.Series(
            {
                'n': n,
                'time': toc - tic,
                'order': len(str(n)),
                'result': resultado_actual
            }
        )
        df.loc[len(df)] = results

    return df




def perf_tests(fn: Callable, max_num: int | float, nargs: int = 1, iterations: int = ITERATIONS) -> pd.DataFrame:
    """
    Tests the performance of functions, giving them random int arguments (with the same number of digits) up to `max`.

    :param fn: Function to test.
    :param max: Maximum allowed number for the tests to be performed.
    :param nargs: Number of arguments of `fn`.
    :param iterations: Number of iterations per digit.

    :return: DataFrame with colums {'a': arg a, ..., 'time': time it took to compute, 'order': number of digits, 'result': result}
    """

    columns = [
        *[ chr(ord('a') + i) for i in range(nargs) ],  # one column per argument: ['a', 'b', ...]
        'time',
        'order',
        'result'
    ]

    df = pd.DataFrame(columns = columns)

    ranges = [(10**i, 10**(i+1) - 1) for i in range(len(str(int(max_num))) - 1)]  # [(1, 99), (10, 999), ...]

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




def plot_performance(numeros: ArrayLike, tiempos: ArrayLike, filename: str, title: str, xlabel: str, ylabel: str, rotation: Annotated[int, "Degrees"] = 0, size: tuple[int, int] = (6, 4), pad_bottom: float | None = None, marker: str = 'o'):
    """
    Plots the performance of a function in a matplotlib graph, and saves it to `IMAGES_OUTPUT_FOLDER/filename`.

    :param numeros: Size of problem (n).
    :param tiempos: Time it took (s).
    :param filename: Name of the file to store.
    :param xlabel: Label of X axis (size of problem).
    :param ylabel: Label of Y axis (time).
    :param rotation: Rotation of ticks, in degrees.
    :param size: Figure size.
    :param pad_bottom: Padding at the bottom of the image.
    :param marker: Matplotlib marker.
    """

    plt.figure(figsize=size)

    # Create a scatter plot
    plt.plot(range(len(numeros)), tiempos, marker=marker, color='blue')

    # Set ticks explicitly
    plt.xticks(range(len(numeros)), [str(num) for num in numeros], rotation=rotation)

    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    plt.subplots_adjust(bottom=pad_bottom)


    # Guardar el gráfico
    plt.savefig(f'{IMAGES_OUTPUT_FOLDER}/{filename}.png')




if __name__ == "__main__":

    ##########
    # PRIMES #
    ##########

    print("\n--- Testing primeslib.is_prime ---\n")
    results_df = perf_tests(primeslib.is_prime, primeslib.MAX_UINT).sort_values(by='a', ignore_index=True).rename(columns={'a': 'n'})

    results_df.to_csv(f'{CSV_OUTPUT_FOLDER}/output_primes.csv')
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

    primes = results_df.loc[results_df['result'] == True]  # get primes
    avgprimes = primes.groupby('order')['time'].mean()  # average per order

    plot_performance(
        avgprimes.index,
        avgprimes.values,
        filename='scatter_plot_primes_only_primes',
        title='Relación entre números primos y Tiempo de Ejecución',
        xlabel='Longitud del Número',
        ylabel='Tiempo de Ejecución (segundos)'
    )

    # Worst cases for primes
    funct_df = func_test(
        primeslib.is_prime,
        [776159, 776161, 98982599, 98982601, 9984605927, 9984605929, 999498062999, 999498063001,99996460031327, 99996460031329, 9999940600088207, 9999940600088209, 999999594000041207, 999999594000041209, 4611685283988009527, 4611685283988009529, 9223371593598182327, 9223371593598182329]
    )

    funct_df.to_csv(f'{CSV_OUTPUT_FOLDER}/output_primes_fucnt_test.csv')
    # funct_df = pd.read_csv(f'{CSV_OUTPUT_FOLDER}/output_primes_fucnt_test.csv')

    plot_performance(
        funct_df['n'],
        funct_df['time'],
        filename='scatter_plot_primes_worst_cases',
        title='Relación entre Longitud del Número y Tiempo de Ejecución en los Peores Casos',
        xlabel='Longitud del Número',
        ylabel='Tiempo de Ejecución (segundos)',
        rotation=90,
        size=(12, 6),
        pad_bottom=0.4
    )



    #######
    # GCD #
    #######

    for fn, name, iterations, max_num in [
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



    ###############
    # THEORETICAL #
    ###############

    # Testeo y representacion de la Función teorica de calculo de primalidad

    def t_primes (n):
        # tiempo ejecución teórico primeslib.is_prime
        return (math.floor(math.sqrt(n)) - 3) / 2


    plot_performance(
        [i+1 for i in range(20)],
        [t_primes(10**i) for i in range(20)],
        filename=f'scatter_plot_primes_theoretical',
        title='Relación entre Longitud del Número y Tiempo de Ejecución Estimado',
        xlabel='Longitud de n',
        ylabel='T(n)',
        marker=""
    )


    # Testeo y representacion de la Función teorica de calculo de MCD por Descomposicion de Factores

    def t_factorize (n):
        # tiempo ejecución teórico gcdlib.gcd_factorize
        return n*2


    plot_performance(
        [i+1 for i in range(20)],
        [t_factorize(10**i) for i in range(20)],
        filename=f'scatter_plot_gcd_theoretical_factorize',
        title='Relación entre Longitud del Número y Tiempo de Ejecución Estimado',
        xlabel='Longitud de n',
        ylabel='T(n)',
        marker=""
    )


    # Testeo y representacion de la Función teorica de calculo de MCD por Euclides

    def t_euclides (n):
        # tiempo ejecución teórico gcdlib.gcd_euclid
        return math.log10(n)


    plot_performance(
        [i+1 for i in range(20)],
        [t_euclides(10**i) for i in range(20)],
        filename=f'scatter_plot_gcd_theoretical_euclid',
        title='Relación entre Longitud del Número y Tiempo de Ejecución Estimado',
        xlabel='Longitud de n',
        ylabel='T(n)',
        marker=""
    )


