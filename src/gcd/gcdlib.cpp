/* GCDLIB MODULE */

#include "gcd.hpp"

#include <pybind11/pybind11.h>

namespace py = pybind11;

PYBIND11_MODULE(gcdlib, m) {

    #ifdef __MINGW32__
    py::options options;
    options.disable_function_signatures();
    #endif

    m.doc() = "C++ Greatest Common Denominator implementations";

    // functions
    m.def(
        "gcd_factorize", &(gcd_factorize<int64_t>),
        "Returns the Greatest Common Denominator in between a and b, using factorization",
        py::arg("a"), py::arg("b")
    );
    m.def(
        "gcd_euclid", &(gcd_euclid<int64_t>),
        "Returns the Greatest Common Denominator in between a and b, the euclidean algorithm",
        py::arg("a"), py::arg("b")
    );
    m.def(
        "gcd_euclid_rec", &(gcd_euclid_rec<int64_t>),
        "Returns the Greatest Common Denominator in between a and b, the recursive euclidean algorithm",
        py::arg("a"), py::arg("b")
    );
}