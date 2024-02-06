/* GCDLIB MODULE */

#include "primes.hpp"

#include <pybind11/pybind11.h>
#include <pybind11/pytypes.h>

namespace py = pybind11;

PYBIND11_MODULE(primeslib, m) {

    #ifdef __MINGW32__
    py::options options;
    options.disable_function_signatures();
    #endif

    m.doc() = "C++ primes checker implementation";

    m.attr("MAX_UINT") = py::cast(-1ULL);

    // functions
    m.def(
        "is_prime", &(is_prime<std::size_t>),
        "Returns true if n is prime, false if it's composite",
        py::arg("n")
    );
}