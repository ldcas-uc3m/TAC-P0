# --------
# PYTHON MODULE
# --------

# create module
pybind11_add_module (gcdlib gcdlib.cpp)

# output module to site-packages folder
set_target_properties (
    gcdlib
    PROPERTIES
        LIBRARY_OUTPUT_DIRECTORY "${CMAKE_SOURCE_DIR}/${PYBIND11_MODULE_OUTPUT_DIRECTORY}"
)



# --------
# CPP LIBRARY
# --------

add_library (gcd INTERFACE gcd.hpp)

# add compilation targets
add_executable (test_gcd "test.cpp")
target_link_libraries (test_gcd PRIVATE gcd)

