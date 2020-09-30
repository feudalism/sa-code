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
        self.mech_obj = None
        self.positions_obj = None
        self.positions = None
        self.num_nodes = 0

        # create pointers to the model's mech. obj. and the positions
        model = kwargs['model']
        self.get_object_pointers(model)

    # def onEvent(self, kwargs):
        # print(" Handling event " + str(kwargs))
            
    def onSimulationInitStartEvent(self, kwargs):
        self.init_print_nodes()
            
    def onSimulationInitDoneEvent(self, kwargs):
        self.create_socket()

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
            
        t = self.root_node.findData('time').value
        if t >= TMAX:
            self.root_node.getRootContext().animate = False
            self.rec_socket.stop()
            print('closing receive socket.')
            
    def get_object_pointers(self, model):
        self.mech_obj = model.mech_obj
        
        ## TODO -- WRONG
        # the following returns the object's position (single point)
        # but I want the all the DOFs
        self.positions_obj = model.mech_obj.findData('position')
        
    def init_print_nodes(self):
        """ Prints number of nodes in the object to be simulated.
            Also creates a socket before the simulation is started.
        """
        self.update_positions()
        self.num_nodes = len(self.positions)
        print(f" Total number of nodes: {self.num_nodes}")
        
    def create_socket(self):
        # create a socket in the first step
        print("t:0.0 \tSTART OF SIMULATION/ANIMATION -- creating TCPReceiveSocket")
        self.rec_socket = TCPReceiveSocket(tcp_port=PORT,
            handler_function=self.set_endnode_y_position)
        self.rec_socket.start(blocking=True)

    def set_endnode_y_position(self, data):
        """ Runs when new data is received from  a send socket.
            Sets the y-position of the final node to the value
            received from the send socket.
        """
        new_y_value = float(data['data'])
        
        endnode_index = self.num_nodes - 1
        
        endnode_desired_position = self.get_node_position(endnode_index)
        endnode_desired_position[1] = new_y_value
        
        self.set_position_at_index(endnode_index, endnode_desired_position)
        
        endnode_new_position = self.get_node_position(endnode_index)
        self.print_2d_coords(endnode_new_position)
        
    def get_node_position(self, n):
        """ Returns current xyz position of the node n."""
        self.update_positions()
        return self.positions[n]
        
    def update_positions(self):
        """ Updates the positions vector (all nodes) from the pointer."""
        self.positions = self.positions_obj.value
        
    def set_position_at_index(self, n, new_position):   
        """ Sets the position of node n to new_position."""
        # get positions as string
        vs = self.positions_obj.getValueString()
        
        # convert to numeric array
        num_array = [float(i) for i in vs.split()]
        
        # replace only the positions of node n
        num_array[n*3] = new_position[0]
        num_array[n*3 + 1] = new_position[1]
        num_array[n*3 + 2] = new_position[2]
        
        # revert to string and set as new position
        vs_new = ' '.join([str(i) for i in num_array])
        self.positions_obj.setValueString(vs_new)
        
    def print_2d_coords(self, node_position):
        """ Prints the time, as well as x- and y-coordinates
            of the given node position."""
        x = node_position[0]
        y = node_position[1]
        t = self.root_node.time.value
        print(f't:{t:2.2f} \t x = {x:2.2f}, y = {y:2.2f}')