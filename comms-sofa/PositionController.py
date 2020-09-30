import Sofa
from settings import TMAX, PORT
from DataSocket import TCPReceiveSocket

import time
    

class PositionController(Sofa.Core.Controller):
    """ Controller that simulates a simple beam and 
        forces the end node's vertical position to a certain value.
        The value is obtained from an external send socket.
    """
    
    def __init__(self, *args, **kwargs):
        # necessary for implementing this class
        # also the normal way to override from a python class
        Sofa.Core.Controller.__init__(self, *args, **kwargs)
        print("Creating the controller...")
        print(f"\tPython::__init__::{str(self.name)}\n")
        self.iterations = 0
        
        # initialise the objects needed for the simulation
        self.root_node = kwargs['root_node']
        self.positions = None
        self.num_nodes = 0

        # creates pointers to the model's mech. obj. and updates the positions
        self.model = kwargs['model']
        self.update_positions_from_object()

    def onEvent(self, kwargs):
        pass
        # print(" Handling event " + str(kwargs))
            
    def onSimulationInitStartEvent(self, kwargs):
        """ Prints number of nodes of the simulation object and
            initialises the receive socket.
        """
        print("Creating TCPReceiveSocket...")
        self.init_print_nodes()
        self.create_socket()
            
    def onSimulationInitDoneEvent(self, kwargs):
        pass

    def onAnimateBeginEvent(self, kwargs):
        """ Pauses between animation steps so that the animation doesn't
            run so quickly.
        """
        # may need to take this out when implementing real-time communication
        self.iterations+=1
        time.sleep(self.root_node.dt.value)

    def onAnimateEndEvent(self, kwargs):
        self.iterations+=1
        
        """ Prints the current coordinates of the end position.
            Once the end time is reached, stops the animation.
        """
        endnode_index = self.num_nodes - 1
        endnode_position = self.get_node_position(endnode_index)
        self.print_2d_coords(endnode_position)
            
        t = self.root_node.time.value
        if t >= TMAX:
            self.root_node.getRootContext().animate = False
            self.rec_socket.stop()
            print('closing receive socket.')
            
    def init_print_nodes(self):
        """ Prints number of nodes in the object to be simulated.
            Also creates a socket before the simulation is started.
        """
        self.update_positions_from_object()
        self.num_nodes = len(self.positions)
        print(f"Total number of nodes: {self.num_nodes}")
        
    def create_socket(self):
        """ Creates a socket in the first step, which runs the handler function
            when new data is received from the SendSocket.
        """
        self.rec_socket = TCPReceiveSocket(tcp_port=PORT,
            handler_function=self.set_endnode_y_position)
        self.rec_socket.start(blocking=True)

    def set_endnode_y_position(self, data):
        """ Runs when new data is received from  a send socket.
            Sets the y-position of the final node to the value
            received from the send socket.
        """
        new_y_value = float(data['data'])
        
        n_endnode = self.num_nodes - 1
        
        endnode_desired_position = self.get_node_position(n_endnode)
        endnode_desired_position[1] = new_y_value # indices 0:x, 1:y, 2:z
        
        self.positions[n_endnode] = endnode_desired_position
        
    def get_node_position(self, n):
        """ Returns current xyz position of the node n."""
        self.update_positions_from_object()
        return self.positions[n]
        
    def update_positions_from_object(self):
        """ Updates the positions vector from the mechanical object."""
        # self.positions_obj = model.mech_obj.findData('position') # Sofa.Core.Data
        self.positions = self.model.mech_obj.position # np.ndarray, writable
        
    def print_2d_coords(self, node_position):
        """ Prints the time, as well as x- and y-coordinates
            of the given node position."""
        x = node_position[0]
        y = node_position[1]
        t = self.root_node.time.value
        print(f't:{t:2.2f} \t x = {x:2.2f}, y = {y:2.2f}')