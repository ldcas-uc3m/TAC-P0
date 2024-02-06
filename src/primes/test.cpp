#include "primes.hpp"

#include <iostream>
#include <cmath>
#include <concepts>
#include <string>
#include <random>
#include <chrono>



template <std::integral UINT_T>
inline void check_random(UINT_T max) {

    std::cout << "Performing tests up to " << max << "\n";

    std::random_device dev;
    std::mt19937 rng(dev());
    std::uniform_int_distribution<std::mt19937::result_type> dist(0, max);


    auto tic = std::chrono::high_resolution_clock::now();

    std::cout << "all good!\n";
    auto toc = std::chrono::high_resolution_clock::now();
    std::cout << "took " << std::chrono::duration_cast<std::chrono::milliseconds>(toc-tic).count() << "ms\n";
}




/* MAIN */

int main(int argc, char* argv[]) {

    switch (argc) {
        case 1:
            check_random(-1ULL);
            return 0;

        case 2:
            return is_prime(std::stoull(argv[1]));

        default:
            std::cerr << "Invalid number of arguments\n";
            return -1;
    }

}