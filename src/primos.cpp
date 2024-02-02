#include <iostream>
#include <chrono>
#include <cstdint>



/**
* @brief checks if a number is prime by seing if it's divisible by any of the already computed primes
*/
bool is_prime(const std::uint64_t & number, const std::vector<std::uint64_t> & primes) {
    for (auto prime : primes) {
        if (number % prime == 0) return false;
    }

    return true;
}


void print_status(
        const std::uint64_t & number,
        const std::vector<std::uint64_t> & primes,
        const std::chrono::_V2::system_clock::time_point & start,
        const std::chrono::_V2::system_clock::time_point & tic,
        const std::chrono::_V2::system_clock::time_point & toc
    ) {

    // current prime number
    std::cout << primes.size() << ": " << number;

    // order of magnitude
    std::cout << std::setfill(' ') << std::setw(16) << std::right;
    std::cout << "10e" << std::to_string(number).length() - 1;

    // time to compute current prime
    std::cout << std::setfill(' ') << std::setw(16) << std::right;
    std::cout << std::chrono::duration_cast<std::chrono::microseconds>(toc-tic).count() << "us";

    // primes per second
    double pps = primes.size() * 10e3 / std::chrono::duration_cast<std::chrono::milliseconds>(toc-start).count();
    std::cout << std::setfill(' ') << std::setw(16) << std::right;
    std::cout << pps << " primes/s";

    // total elapsed time
    std::cout << std::setfill(' ') << std::setw(16) << std::right;
    std::cout << std::chrono::duration_cast<std::chrono::seconds>(toc-start).count() << "s";

    std::cout << '\n';
}



int main() {
    /*
    Brute-force dynamic programming solution:
    Hold all prime numbers (except 1) in a vector, go through all numbers.
        - If the number it's divisible by any of the previous prime numbers, then it's not a prime number
        - Else, add it to the vector and continue.
    */

    std::vector<std::uint64_t> primes {2};  // list of found primes

    auto start = std::chrono::high_resolution_clock::now();

    const std::uint64_t MAX_LONG = -1;
    for (std::uint64_t i = 3; i < MAX_LONG; i += 2) {
        auto tic = std::chrono::high_resolution_clock::now();

        if (is_prime(i, primes)) {
            auto toc = std::chrono::high_resolution_clock::now();

            primes.push_back(i);  // add to the list of primes

            print_status(i, primes, start, tic, toc);
        }
    }

      // MAX_LONG is not a prime

    std::cout << "Reached the limit of std::uint64_t (" << MAX_LONG << ")." << '\n';
    std::cout << "For even bigger numbers, but worse performance, use primes_inf." << '\n';

    return 0;
}