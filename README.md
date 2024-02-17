# Práctica 0: Ejercicios Prácticos Introductorios
By Ignacio Arnaiz Tierraseca & Luis Daniel Casais Mezquida  
Teoría avanzada de la computación 23/24  
Bachelor's Degree in Computer Science and Engineering  
Universidad Carlos III de Madrid


## Project statement

### EJERCICIO PRÁCTICO 1: Cálculo del máximo común divisor de 2 números.
Se pide programar y evaluar dos formas alternativas de determinar los factores comunes a dos números.
1. Desarrolla el código fuente para los algoritmos que se indican a continuación:
    1. **Algoritmo 1**: Descomposición de los números en sus factores primos, y multiplicación de los factores comunes con el menor exponente.
    2. **Algoritmo 2**: Método de Euclides.

    Las entradas son dos números naturales. La salida es el máximo común divisor.

2. Determina experimentalmente (empíricamente) la complejidad computacional deambos algoritmos. En ambos casos debes realizar el análisis considerando como tamaño de entrada el número de dígitos de las dos entradas. Es decir, determina la complejidad realizando pruebas de ejecución (desde valores pequeños a los valoresmáximos que te permita la representación de números según los tipos empleados), midiendo el tiempo empleado en la ejecución. Puedes elaborar los scripts o ficheros por lotes que necesites para generar los datos y/o los gráficos. Además, puedes emplear el lenguaje de programación o _framework_ (e.g. Matlab, R, Python, etc.) que desees para generar los datos y capturar los resultados.  
**Importante:** Para generar la gráficas, puedes emplear el lenguaje de programación o _framework_ (e.g. Matlab, R, Python, etc.), o herramientas SW (e.g. MS Excel), que muestren los resultados, es decir, tamaño de entrada (eje de abscisas) frente al tiempo deejecución (eje de ordenadas).  
Detalla razonadamente la experimentación realizada y las conclusiones obtenidas.  
Debes llevar a cabo un número de pruebas suficiente para obtener resultados significativos que te apoyen en las conclusiones. Es conveniente que las gráficas tengan sentido, sean significativas, etc. Plantea alternativas para obtener resultados lo más fiables posibles.
3. Realiza una evaluación analítica de ambos algoritmos. Explica razonadamente tus argumentos. ¿Qué conclusiones obtienes de este estudio analítico? Compara los resultados del estudio experimental y del estudio analítico, ¿qué conclusiones obtienes?
4. Presenta tus resultados en una memoria, en forma académica: (a) Resumen, (b) Introducción, (c) Desarrollo, (d) Conclusiones, (e) Referencias. No olvides identificar tus tablas y gráficas con un número y un título.


### EJERCICIO PRÁCTICO 2. Cómputo de la primalidad de un número natural.
Desarrolla en código fuente un algoritmo, _que tú mismo diseñes_, que compute si un número natural es primo o compuesto. Puedes diseñar varios algoritmos (o versiones, mejoras, de un mismo algoritmo).

De la misma manera que en el [Ejercicio Práctico 1](#ejercicio-práctico-1-cálculo-del-máximo-común-divisor-de-2-números), obtén analíticamente y experimentalmente la complejidad computacional del (los) algoritmo(s) que implementes en tu código fuente.
Detalla, razonadamente, la experimentación realizada y las conclusiones obtenidas.

Presenta tus resultados en una memoria, con las características descritas en el ejercicio práctico 1.



## Instalation and execution

1. Create a Python virtual enviroment in the `venv` folder.
    ```bash
    python3 -m venv ./venv
    ```
2. Activate the venv
   - Linux:
        ```bash
        source venv/bin/activate
        ```
    - Windows (PowerShell):
        ```powershell
        & .\venv\Scripts\Activate.ps1
        ```
3. Install the dependencies
   ```
   pip install -r requirements.txt
   ```
4. Build the C++ libraries. This will install the modules in your venv.
    - Linux:
        ```bash
        cd build/
        cmake ..
        make
        cd ..
        ```
    - Windows
        ```powershell
        cd build/
        cmake .. -G Ninja
        cmake --build .
        cd ..
        ```
5. Run the script.
    ```
    python3 src/test.py
    ```

### C++ Compiler
For the compiler, we recomend GCC >= 11, as we use some C++20 & C++23 features.

If you're in Windows, we recommend you to instal [WSL2](https://learn.microsoft.com/es-es/windows/wsl/install) and run "in Linux", or use GCC through [MinGW-W64](https://www.mingw-w64.org/), you can find compiled binaries [here](https://github.com/niXman/mingw-builds-binaries).
