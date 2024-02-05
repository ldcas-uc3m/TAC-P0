#ifndef GCD_HPP
#define GCD_HPP


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
std::map<INT_T, int> _factorize(INT_T n) {

    std::map<INT_T, int> factors {};  // prime factors and their exponents

    INT_T i = 2;  // current factor
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


// std::abs with support for unsigned ints
template <std::unsigned_integral UINT_T>
constexpr UINT_T _abs(UINT_T n) { return n; }

template <std::integral INT_T>
constexpr INT_T _abs(INT_T n) { return std::abs(n); }


template <std::integral INT_T>
/**
* @brief Returns the Greatest Common Denominator in between a and b
*/
INT_T gcd_factorize(const INT_T a, const INT_T b) {

    // base cases
    if (b == 0)
        return a;

    if (a == 0)
        return b;

    if (a == b)
        return a;


    // get factors for both numbers
    std::map<INT_T, int> factors_a = _factorize(_abs(a));
    std::map<INT_T, int> factors_b = _factorize(_abs(b));


    // set up `n` and `m` so `m` is the one with smallest number of factors
    std::map<INT_T, int> factors_n, factors_m;
    if (factors_a.size() > factors_b.size()) {
        factors_n = std::move(factors_a);
        factors_m = std::move(factors_b);
    }
    else {
        factors_n = std::move(factors_b);
        factors_m = std::move(factors_a);
    }

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

#endif