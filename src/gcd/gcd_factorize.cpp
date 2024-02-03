#include <iostream>
#include <chrono>
#include <cmath>
#include <iterator>
#include <concepts>
#include <map>
#include <stdexcept>
#include <numeric>

#include <random>



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
INT_T mcd(INT_T a, INT_T b) {

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



inline void test_many(std::size_t max) {
    std::random_device dev;
    std::mt19937 rng(dev());
    std::uniform_int_distribution<std::mt19937::result_type> dist(0, max);

    for (std::size_t _ = 0; _ < max; ++_) {
        std::size_t a = dist(rng);
        std::size_t b = dist(rng);

        if (std::gcd(a, b) != mcd(a, b)) {
            std::cout << "ERROR in ";
            std::cout << "a=" << a << "; b=" << b << "\n";
            std::cout << "STL: " << std::gcd(a, b) << "; ";
            std::cout << "US: " << mcd(a, b) << "\n";

            return;
        }
    }
}


inline void test_one(std::size_t a, std::size_t b) {
    std::cout << "a=" << a << "; b=" << b << "\n";
    std::cout << "STL: " << std::gcd(a, b) << "; ";
    std::cout << "US: " << mcd(a, b) << "\n";
}


int main() {

    test_many(76878);
    std::cout << "all good!\n";

    return 0;
}