
/* iegenlib.i */
%module iegenlib

%{
#define SWIG_FILE_WITH_INIT
#include "src/computation/Computation.h"
%}

%include "std_string.i"
%include "std_array.i"
%include "numpy.i"
%include "typemaps.i"
%include "std_vector.i"

%init %{
    import_array();
%}
%include "src/computation/Computation.h"
