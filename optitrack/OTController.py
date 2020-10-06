import Sofa

class OTController(Sofa.Core.Controller):

    def __init__(self, *args, **kwargs):
        # necessary for implementing this class
        # also the normal way to override from a python class
        Sofa.Core.Controller.__init__(self, *args, **kwargs)
        print("Creating the OptiTrack controller...")
        print(f"\tPython::__init__::{str(self.name)}\n")
        self.iterations = 0
        
        # initialise the objects needed for the simulation
        self.root_node = kwargs['root']
            
    def onSimulationInitStartEvent(self, kwargs):
        """ Prints number of nodes of the simulation object and
            initialises the receive socket.
        """
        pass
            
    def onSimulationInitDoneEvent(self, kwargs):
        pass