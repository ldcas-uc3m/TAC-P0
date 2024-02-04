#ifndef GCD_HPP
#define GCD_HPP


#include <concepts>
#include <map>



template <std::integral INT_T>
/**
* @brief Returns the prime factorials of a natural number n, and their exponents (frequency)
*/
std::map<INT_T, INT_T> factorize(INT_T n);


template <std::integral INT_T>
/**
* @brief Returns the Greatest Common Denominator in between a and b
*/
INT_T gcd_factorize(INT_T a, INT_T b);



template <std::integral INT_T>
/**
* @brief Returns the Greatest Common Denominator in between a and b
*/
INT_T gcd_euclid(INT_T a, INT_T b);


template <std::integral INT_T>
/**
* @brief Returns the Greatest Common Denominator in between a and b
*/
INT_T gcd_euclid_rec(INT_T a, INT_T b);


#endif