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


/* TESTS */

template <std::integral INT_T>
void check_many(INT_T max) {

    std::cout << "performing tests up to " << max << "...\n";

    std::random_device dev;
    std::mt19937 rng(dev());
    std::uniform_int_distribution<std::mt19937::result_type> dist(0, max);

    auto tic = std::chrono::high_resolution_clock::now();

    for (INT_T _ = 0; _ < max; ++_) {
        INT_T a = dist(rng);
        INT_T b = dist(rng);

        INT_T result1 = gcd_factorize(a, b);

        if (std::gcd(a, b) != result1) {
            std::cout << "ERROR: ";
            std::cout << "a=" << a << "; b=" << b << "\n";
            std::cout << "STL: " << std::gcd(a, b) << "; ";
            std::cout << "US: " << result1 << "\n";

            return;
        }
    }

    std::cout << "all good!\n";

    auto toc = std::chrono::high_resolution_clock::now();
    std::cout << "took " << std::chrono::duration_cast<std::chrono::milliseconds>(toc-tic).count() << "ms\n";
}


template <std::integral INT_T>
void check_one(INT_T a, INT_T b) {
    std::cout << "a=" << a << "; b=" << b << "\n";
    std::cout << "std::gcd: " << std::gcd(a, b) << "; ";
    std::cout << "gcd_factorize: " << gcd_factorize(a, b) << "\n";
}



/* MAIN */

int main(int argc, char* argv[]) {

    switch (argc) {
        case 1:
            check_many(static_cast<std::size_t>(std::pow(2, 16)));
            return 0;

        case 2:
            check_many(static_cast<std::size_t>(std::pow(2, std::stoll(argv[1]))));
            return 0;

        case 3:
            std::cout << gcd_factorize(std::stoll(argv[1]), std::stoll(argv[2])) << "\n";
            return 0;

        default:
            std::cerr << "Invalid number of arguments\n";
            return -1;
    }

}