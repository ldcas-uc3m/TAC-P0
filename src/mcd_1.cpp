#include <iostream>
#include <chrono>
#include <cstdint>
#include <cmath>
#include <iterator>
#include <random>



inline std::size_t gimme_random(std::size_t max) {
    std::random_device dev;
    std::mt19937 rng(dev());
    std::uniform_int_distribution<std::mt19937::result_type> dist(0, max);

    return dist(rng);
}


/**
* @brief checks if a number is prime by seing if it's divisible by any of the already computed primes
*/
bool is_prime(const std::size_t & number, const std::vector<std::size_t> & primes) {

    for (auto prime : primes) {
        if (number % prime == 0) return false;
    }

    return true;
}


std::size_t mcd(std::size_t a, std::size_t b) {

    // base cases
    if (
        (a == 0)
        || (b == 0)
    ) {
        return 0;
    }

    if (
        (a == 1)
        || (b == 1)
    ) {
        return 1;
    }


    std::vector<std::uint64_t> primes {2};  // list of primes
    std::size_t n;  // bigger number
    std::size_t m;  // smaller number

    if (a > b){
        n = a;
        m = b;
    }
    else if (b > a) {
        n = b;
        m = a;
    }
    else { // a = b
        n = a;
        m = b;
    }


    // compute primes up to n

    for (std::size_t i = 3; i <= n; ++i) {
        if (is_prime(i, primes))
            primes.push_back(i);  // add to list of primes
    }


    if (a == b) {
        return primes.back();
    }

    // go through list of primes until you find one that's not prime

    std::vector<std::uint64_t> common_primes {};  // list of common primes

    for (auto it = primes.begin(); it != primes.end(); ++it) {
        if (*it >= m) break;

        if (
            (m % *it == 0)
            && (n % *it == 0)
        ) {  // common divisor
            common_primes.push_back(*it);  // add to list
        }
    }

    if (common_primes.size() == 0)
        return 1;
    else
        return common_primes.back();
}



int main() {

    const std::size_t MAX = 256;

    std::size_t a = gimme_random(MAX);
    std::size_t b = gimme_random(MAX);

    // a=204; b=208
    // int a = 98;
    // int b = 114;

    std::cout << "a=" << a << "; b=" << b << "\n";
    std::cout << "STL: " << std::gcd(a, b) << "    ";
    std::cout << "us: " << mcd(a, b) << "\n";

    return 0;
}