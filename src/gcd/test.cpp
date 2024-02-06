#include "gcd.hpp"

#include <iostream>
#include <cmath>
#include <concepts>
#include <string>
#include <random>
#include <chrono>



template <std::integral INT_T>
int check_many(INT_T max) {

    std::cout << "Performing tests up to " << max << "\n";

    std::random_device dev;
    std::mt19937 rng(dev());
    std::uniform_int_distribution<std::mt19937::result_type> dist(0, max);


    /* GCD factorize */
    std::cout << "testing gcd_factorize...\n";
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

            return -1;
        }
    }
    auto toc = std::chrono::high_resolution_clock::now();

    std::cout << "all good!\n";
    std::cout << "took " << std::chrono::duration_cast<std::chrono::milliseconds>(toc-tic).count() << "ms\n";


    /* GCD euclidean */
    std::cout << "testing gcd_euclid...\n";

    tic = std::chrono::high_resolution_clock::now();

    for (INT_T _ = 0; _ < max; ++_) {
        INT_T a = dist(rng);
        INT_T b = dist(rng);

        INT_T result1 = gcd_euclid(a, b);

        if (std::gcd(a, b) != result1) {
            std::cout << "ERROR: ";
            std::cout << "a=" << a << "; b=" << b << "\n";
            std::cout << "STL: " << std::gcd(a, b) << "; ";
            std::cout << "US: " << result1 << "\n";

            return -1;
        }
    }

    toc = std::chrono::high_resolution_clock::now();

    std::cout << "all good!\n";
    std::cout << "took " << std::chrono::duration_cast<std::chrono::milliseconds>(toc-tic).count() << "ms\n";

    return 0;
}


template <std::integral INT_T>
void check_one(INT_T a, INT_T b) {
    std::cout << "a=" << a << "; b=" << b << "\n";
    std::cout << "std::gcd: " << std::gcd(a, b) << "; ";
    std::cout << "gcd_euclid: " << gcd_euclid<INT_T>(a, b) << "\n";
}



/* MAIN */

int main(int argc, char* argv[]) {

    switch (argc) {
        case 1:
            return check_many(static_cast<std::size_t>(std::pow(2, 16)));

        case 2:
            return check_many(static_cast<std::size_t>(std::pow(2, std::stoll(argv[1]))));

        case 3:
            std::cout << gcd_factorize(std::stoll(argv[1]), std::stoll(argv[2])) << "\n";
            return 0;

        default:
            std::cerr << "Invalid number of arguments\n";
            return -1;
    }

}