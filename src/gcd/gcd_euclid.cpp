#include <iostream>
#include <cmath>
#include <concepts>
#include <string>
#include <random>
#include <chrono>



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

        INT_T result1 = gcd_euclid(a, b);

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
    std::cout << "gcd_euclid: " << gcd_euclid(a, b) << "\n";
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
            std::cout << gcd_euclid(std::stoll(argv[1]), std::stoll(argv[2])) << "\n";
            return 0;

        default:
            std::cerr << "Invalid number of arguments\n";
            return -1;
    }

}