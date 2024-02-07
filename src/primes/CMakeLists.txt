# --------
# PYTHON MODULE
# --------

# create module
pybind11_add_module (primeslib primeslib.cpp)

# output module to site-packages folder
set_target_properties (
    primeslib
    PROPERTIES
        LIBRARY_OUTPUT_DIRECTORY "${CMAKE_SOURCE_DIR}/${PYBIND11_MODULE_OUTPUT_DIRECTORY}"
)



# --------
# CPP LIBRARY
# --------

add_library(primes INTERFACE primes.hpp)

# add compilation targets
add_executable(test_primes "test.cpp")
target_link_libraries (test_primes PRIVATE primes)

