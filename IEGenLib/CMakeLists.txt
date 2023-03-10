cmake_minimum_required(VERSION 2.8)
project(IEGENLIB)

## Add a 'docs' target to build documentation.  (make docs)
add_subdirectory(doc)

#Tell cmake to look in Modules for custom modules
set(CMAKE_MODULE_PATH
    ${CMAKE_CURRENT_SOURCE_DIR}/cmake/modules
    ${CMAKE_MODULE_PATH})

## ensure that we are doing an out of source build
include(MacroOutOfSourceBuild)
macro_ensure_out_of_source_build(
    "${PROJECT_NAME} requires an out of source build.")

set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)

enable_testing()

## add the includes and libaries that we depend on
find_package(Threads)
include_directories(${Threads_INCLUDE_DIR})

## add in dependencies
include(ExternalProject)
ExternalProject_Add(libgmp
    DOWNLOAD_COMMAND ""
    SOURCE_DIR ${CMAKE_CURRENT_SOURCE_DIR}/lib/gmp
    BUILD_IN_SOURCE ON
    CONFIGURE_COMMAND autoreconf -f -i
    COMMAND ./configure --prefix=${CMAKE_CURRENT_SOURCE_DIR}/lib/installed --disable-shared --with-pic
    BUILD_COMMAND ${MAKE})

ExternalProject_Add(lib-omega
    GIT_REPOSITORY "https://github.com/BoiseState-AdaptLab/omega"
    GIT_TAG "e0e5d046dac0b99cbf17711f168728081b23dea9"
    GIT_PROGRESS ON
    SOURCE_DIR ${CMAKE_CURRENT_SOURCE_DIR}/lib/omega
    BUILD_IN_SOURCE ON
    CONFIGURE_COMMAND autoreconf -f -i
    COMMAND ./configure --prefix=${CMAKE_CURRENT_SOURCE_DIR}/lib/installed
    BUILD_COMMAND make CFLAGS=-fPIC CXXFLAGS=-fPIC VERBOSE=1
    # BUILD_COMMAND make
    # INSTALL_COMMAND make install
)

ExternalProject_Add(lib-isl
    DOWNLOAD_COMMAND ""
    DEPENDS libgmp lib-omega
    SOURCE_DIR ${CMAKE_CURRENT_SOURCE_DIR}/lib/isl
    BUILD_IN_SOURCE ON
    CONFIGURE_COMMAND autoreconf -f -i
    COMMAND ./configure --prefix=${CMAKE_CURRENT_SOURCE_DIR}/lib/installed --with-int=imath-32 --disable-shared --with-pic
    BUILD_COMMAND ${MAKE})

## -I and -L on external projects
include_directories(${IEGENLIB_SOURCE_DIR}/lib/omega/install/include)
link_directories(${IEGENLIB_SOURCE_DIR}/lib/omega/install/lib)
include_directories(${IEGENLIB_SOURCE_DIR}/lib/installed/include)
link_directories(${IEGENLIB_SOURCE_DIR}/lib/installed/lib)
include_directories(${IEGENLIB_SOURCE_DIR}/lib/gtest/include)

## gtest is added through lib (our source through src)
add_subdirectory(lib)
add_subdirectory(src)
add_subdirectory(tutorial)

## set up the testing
add_custom_command(OUTPUT iegen_lib_gdbtest
    COMMAND IEGEN_HOME=. gdb src/iegenlib_t
    DEPENDS iegenlib_t
    COMMENT "Run iegenlib tests through gdb")
add_custom_target(gdbtest DEPENDS iegen_lib_gdbtest)

add_custom_command(OUTPUT iegen_lib_memtest
    COMMAND IEGEN_HOME=. valgrind --leak-check=full src/iegenlib_t
    DEPENDS iegenlib_t
    COMMENT "Run iegenlib tests through valgrind for memory error detection")
add_custom_target(mtest DEPENDS iegen_lib_memtest)

add_custom_command(OUTPUT iegen_lib_test
	          COMMAND IEGEN_HOME=. bin/iegenlib_t
                  DEPENDS iegenlib_t
                  COMMENT "Run iegenlib tests")
add_custom_target(rtest DEPENDS iegen_lib_test)

# Set flags for various builds.
set(CMAKE_CXX_FLAGS "-std=c++11 -fPIC"
    CACHE STRING "Flags used by the compiler during all build types." FORCE)
set(CMAKE_CXX_FLAGS_RELEASE "-std=c++11 -O3 -DNDEBUG"
    CACHE STRING "Flags used by the compiler during release builds." FORCE)
set(CMAKE_CXX_FLAGS_DEBUG  "-std=c++11 -O0 -g"
    CACHE STRING "Flags used by the compiler during debug builds." FORCE)
set(CMAKE_EXE_LINKER_FLAGS_DEBUG  "-std=c++11 -fPIC -O0 -g"
    CACHE STRING "Flags used by the linker during debug builds." FORCE)
set( CMAKE_MODULE_LINKER_DEBUG_FLAGS "-std=c++11 -fPIC -O0 -g" CACHE STRING "" FORCE )
set( CMAKE_SHARED_LINKER_DEBUG_FLAGS "-std=c++11 -fPIC -O0 -g" CACHE STRING "" FORCE )
