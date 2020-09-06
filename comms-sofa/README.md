# comms-sofa
Communicating with SOFA using [PyDataSocket](https://github.com/psomers3/PyDataSocket).

Here, a minimal simulation using a beam is carried out.
At every time step, the end node of the beam
is forced to the position value transmitted
from the SendSocket.

![](/raw/python2/comms-sofa/start.PNG)
![](/raw/python2/comms-sofa/end.PNG)

# Requirements
* Python 2
* [PyDataSocket](https://github.com/psomers3/PyDataSocket)
* numpy