# CMake generated Testfile for 
# Source directory: /home/KALYANBHETWAL/IEGenLib_kalyan/IEGenLib/src
# Build directory: /home/KALYANBHETWAL/IEGenLib_kalyan/IEGenLib/build/src
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(iegenlib_unit_test "iegenlib_t")
set_tests_properties(iegenlib_unit_test PROPERTIES  ENVIRONMENT "IEGEN_HOME=/home/KALYANBHETWAL/IEGenLib_kalyan/IEGenLib/build" _BACKTRACE_TRIPLES "/home/KALYANBHETWAL/IEGenLib_kalyan/IEGenLib/src/CMakeLists.txt;198;add_test;/home/KALYANBHETWAL/IEGenLib_kalyan/IEGenLib/src/CMakeLists.txt;0;")
subdirs("bindings")
