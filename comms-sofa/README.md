# comms-sofa
Communicating with SOFA using [PyDataSocket](https://github.com/psomers3/PyDataSocket).

----

Here, a minimal simulation using a beam is carried out.
At every time step, the end node of the beam
is forced to the position value transmitted
from the SendSocket.

![](https://github.com/feudalism/sa-code/raw/python2/comms-sofa/start.PNG)
![](https://github.com/feudalism/sa-code/raw/python2/comms-sofa/end.PNG)

## To run
    python ./sofa_set_position.py

## Requirements
* [SOFA](https://www.sofa-framework.org/)
* Python 3
* [PyDataSocket](https://github.com/psomers3/PyDataSocket)
* numpy