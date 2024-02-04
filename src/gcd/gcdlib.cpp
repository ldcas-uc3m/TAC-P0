#include <iostream>
#include <cmath>
#include <concepts>
#include <map>
#include <stdexcept>
#include <string>
#include <random>
#include <chrono>



template <std::integral INT_T>
/**
* @brief Returns the prime factorials of a natural number n, and their exponents (frequency)
*/
std::map<INT_T, INT_T> factorize(INT_T n) {
    if (n <= 0) throw std::invalid_argument("n must be bigger than 0");

    INT_T i = 2;
    std::map<INT_T, INT_T> factors {};  // prime factors and their exponents

    while (n > 1) {
        if (n % i == 0) {  // found a prime factor

            // update exponent
            if (factors.contains(i))
                ++factors[i];
            else
                factors.insert({i, 1});

            n /= i;
        }
        else ++i;
    }

    return factors;
}


template <std::integral INT_T>
/**
* @brief Returns the Greatest Common Denominator in between a and b
*/
INT_T gcd_factorize(INT_T a, INT_T b) {

    // base cases

    if (b == 0)
        return a;

    if (a == 0)
        return b;

    if (a == b)
        return a;

    if ((a <= 1) || (b <= 1))
        return 1;


    // figure out biggest and smallest number
    INT_T n = std::max(a, b);
    INT_T m = std::min(a, b);


    // get factors for both numbers
    std::map<INT_T, INT_T> factors_n = factorize(n);
    std::map<INT_T, INT_T> factors_m = factorize(m);


    // go through the factors of m, if it's a common factor, multiply the result by the factor to the smallest exponent

    INT_T res = 1;

    for (const auto & [factor, exponent] : factors_m) {
        if (factors_n.contains(factor))
            res *= std::pow(factor, std::min(exponent, factors_n[factor]));
    }

    return res;
}


template <std::integral INT_T>
/**
* @brief Returns the Greatest Common Denominator in between a and b
*/
INT_T gcd_euclid(INT_T a, INT_T b) {
    if (a == b) return a;

    while (b > 0) {
        INT_T r = a % b;

        // gcd_euclid(m, r)
        a = b;
        b = r;
    }

    return a;
}


template <std::integral INT_T>
/**
* @brief Returns the Greatest Common Denominator in between a and b
*/
INT_T gcd_euclid_rec(INT_T a, INT_T b) {
    if (b == 0) return a;

    return gcd_euclid_rec(b, a % b);
}




// pybind11
#ifdef PYBIND11

#include <pybind11/pybind11.h>

namespace py = pybind11;

PYBIND11_MODULE(gcdlib, m) {

    #ifdef __MINGW32__
    py::options options;
    options.disable_function_signatures();
    #endif

    m.doc() = "C++ Greatest Common Denominator implementations";

    // functions
    m.def(
        "gcd_factorize", &(gcd_factorize<int64_t>),
        "Returns the Greatest Common Denominator in between a and b, using factorization",
        py::arg("a"), py::arg("b")
    );
    m.def(
        "gcd_euclid", &(gcd_euclid<int64_t>),
        "Returns the Greatest Common Denominator in between a and b, the euclidean algorithm",
        py::arg("a"), py::arg("b")
    );
    m.def(
        "gcd_euclid_rec", &(gcd_euclid_rec<int64_t>),
        "Returns the Greatest Common Denominator in between a and b, the recursive euclidean algorithm",
        py::arg("a"), py::arg("b")
    );
}

#endif