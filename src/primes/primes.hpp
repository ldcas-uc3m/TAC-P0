#ifndef PRIMES_HPP
#define PRIMES_HPP


#include <cmath>
#include <concepts>


template <std::unsigned_integral UINT_T>
/**
* @brief Returns true if n is prime, false if it's composite
*/
bool is_prime(UINT_T n) {

    if (n % 2 == 0) return false;

    const UINT_T SQRT_N = std::floor(std::sqrt(n));
    for (UINT_T i = 3; i <= SQRT_N; i += 2) {
        if (n % i == 0) return false;
    }

    return true;
}



#endif