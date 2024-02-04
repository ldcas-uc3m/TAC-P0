# py library (pybind11)

# get pybind11
include(FetchContent)
FetchContent_Declare (
    pybind11
    URL https://github.com/pybind/pybind11/archive/refs/tags/v2.11.1.tar.gz
)
FetchContent_MakeAvailable (pybind11)

# create module
pybind11_add_module (gcdlib gcdlib.cpp)
target_compile_definitions(gcdlib PUBLIC PYBIND11)  # enable pybind in gcdlib.cpp

# output lib to venv
set_target_properties (
    gcdlib
    PROPERTIES
    LIBRARY_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/venv
)



# # add cpp library
# add_library(gcd STATIC)

# target_sources (
#     gcd

#     PUBLIC
#         gcd.hpp
#     PRIVATE
#         gcdlib.cpp
# )

# # add compilation targets
# add_executable(test "test.cpp")
# target_link_libraries (test PRIVATE gcd)

