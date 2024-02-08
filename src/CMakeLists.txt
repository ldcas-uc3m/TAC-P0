# --------
# PYBIND11
# --------

find_package (Python REQUIRED COMPONENTS Interpreter Development)


# get pybind11
include(FetchContent)
FetchContent_Declare (
    pybind11
    URL https://github.com/pybind/pybind11/archive/refs/tags/v2.11.1.tar.gz
)
FetchContent_MakeAvailable (pybind11)



# locate site-packages folder
if (NOT EXISTS "${CMAKE_SOURCE_DIR}/venv")
    message (WARNING "Python Virtual enviroment (${CMAKE_SOURCE_DIR}/venv/) not found")
endif()

if (WIN32)
    set (PYBIND11_MODULE_OUTPUT_DIRECTORY "venv/Lib/site-packages")
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

add_subdirectory(gcd)
add_subdirectory(primes)

