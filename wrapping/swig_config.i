%module DefSLAM
%{
#define SWIG_FILE_WITH_INIT
#include "Edge.h"
#include "Node.h"
#include "MapPoint.h"
#include "Map.h"
#include "Template.h"
%}
%include "Edge.h"
%include "Node.h"
%include "MapPoint.h"
%include "Map.h"
%include "Template.h"