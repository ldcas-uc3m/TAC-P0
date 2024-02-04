# --------
# PYTHON MODULE
# --------

find_package (Python3 REQUIRED COMPONENTS Interpreter Development)

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



# locate site-packages folder
if (WIN32)
    set (GCDLIB_OUTPUT_DIRECTORY "venv/Lib/site-packages")
endif ()

if (UNIX)
    if (NOT DEFINED ${PYTHON_EXECUTABLE})
        set (GCDLIB_OUTPUT_DIRECTORY "src/gcd")
    else()
        exec_program (
            ${PYTHON_EXECUTABLE}
            ARGS "-c \"print('venv/lib/' + 'python' + '.'.join('${PYTHON_VERSION}'.split('.')[:-1]) + '/site-packages')\""
            OUTPUT_VARIABLE GCDLIB_OUTPUT_DIRECTORY
        )
    endif()
endif ()

# output module to site-packages folder
set_target_properties (
    gcdlib
    PROPERTIES
        LIBRARY_OUTPUT_DIRECTORY "${CMAKE_SOURCE_DIR}/${GCDLIB_OUTPUT_DIRECTORY}"
)



# --------
# CPP LIBRARY
# --------

add_library(gcd INTERFACE gcd.hpp)

# add compilation targets
add_executable(test "test.cpp")
target_link_libraries (test PRIVATE gcd)

