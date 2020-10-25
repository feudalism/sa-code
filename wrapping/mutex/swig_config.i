%module DefSLAM
%{
#define SWIG_FILE_WITH_INIT
#include "MapPoint.h"
%}
%feature("immutable", 1) MapPoint::mGlobalMutex;
%typemap(out, optimal="1") mutex %{
  $result = SWIG_NewPointerObj(($1_ltype*)&$1, $&1_descriptor, 0);
%}      
%include "MapPoint.h"