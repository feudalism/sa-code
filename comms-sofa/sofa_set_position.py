# import os, sys, time

from settings import PORT, TMAX, VERBOSE, SOFA_INSTALL_DIR

import SofaRuntime
import Sofa
from SofaRuntime import PluginRepository

from BeamMin import BeamMin as Beam


# import Sofa.Gui
# from DataSocket import TCPReceiveSocket

def create_scene(root_node):
    # controller
    pos_controller = PositionController(name="pos_controller",
                            root_node=root_node)
    root_node.addObject(pos_controller)
        
    # simulation settings
    root_node.gravity = [0, 0., 0]
    root_node.dt = 1
    
    # visuals
    root_node.addObject('VisualStyle',
        displayFlags='showVisual showWireframe showBehaviorModels')
    
    # solver
    root_node.addObject('EulerImplicit',
        name='cg_odersolver',
        printLog='false')
    root_node.addObject('CGLinearSolver',
        name='linear solver',
        iterations=25,
        tolerance=2.0e-9,
        threshold=1.0e-9)
    
    # animation
    root_node.addObject("DefaultAnimationLoop", name="loop")

class PositionController(Sofa.Core.Controller):
    """ Controller that simulates a simple beam and 
        forces the end node's vertical position to a certain value.
        The value is obtained from an external send socket.
    """
    
    def __init__(self, *args, **kwargs):
        ## These are needed (and the normal way to override from a python class)
        Sofa.Core.Controller.__init__(self, *args, **kwargs)
        print(" Python::__init__::"+str(self.name))
        self.inited = 0
        self.iterations = 0
        
        #custom
        """ Initialises the objects needed for the simulation. """
        self.root_node = kwargs['root_node']
        self.mech_obj = None
        self.positions_obj = None
        self.positions = None
        self.num_nodes = 0
        
        beam = Beam(self.root_node, 'deformableBeam')

        # # create pointers
        # self.mech_obj = beam.main_node.getObject('DOFs')
        # self.positions_obj = self.mech_obj.getData('position')

    def __del__(self):
            print(" Python::__del__")
    
    def init(self):
            print(" Python::init() at "+str(self))
            self.inited += 1

    def onEvent(self, kwargs):
            print(" Handling event " + str(kwargs))

    def onAnimateBeginEvent(self, kwargs):
            print(" Python::onAnimationBeginEvent() ("+str(kwargs) + ")")
            self.iterations+=1

    def onAnimateEndEvent(self, kwargs):
            print(" Python::onAnimateEndEvent() ("+str(kwargs) + ")")
            self.iterations+=1
        
    def createGraph(self, root_node):
        """ Initialises the objects needed for the simulation. """
        self.root_node = root_node
        # self.mech_obj = None
        # self.positions_obj = None
        # self.positions = None
        self.num_nodes = 0
        
        print("createGraph is run")
        
        # beam = Beam(root_node, 'deformableBeam')

        # # create pointers
        # self.mech_obj = beam.main_node.getObject('DOFs')
        # self.positions_obj = self.mech_obj.getData('position')
        
    def bwdInitGraph(self, root_node):
        """ Prints number of nodes in the object to be simulated.
            Also creates a socket before the simulation is started.
        """
        # self.update_positions()
        # self.num_nodes = len(self.positions)
        print(f"Total number of nodes {self.num_nodes}")
        
        # # create a socket in the first step
        # print("t:0.0 \tSTART OF SIMULATION/ANIMATION")
        # self.rec_socket = TCPReceiveSocket(tcp_port=PORT,
            # handler_function=self.set_endnode_y_position)
        # self.rec_socket.start(blocking=True)

    # def onBeginAnimationStep(self, dt):
        # """ Pauses between animation steps so that the animation doesn't
            # run so quickly.
        # """
        # # may need to take this out when implementing real-time communication
        # time.sleep(dt)
    
    # def onEndAnimationStep(self, dt):
        # """ Prints the current coordinates of the end position.
            # Once the end time is reached, stops the animation.
        # """
        # endnode_index = self.num_nodes - 1
        # endnode_position = self.get_node_position(endnode_index)
        # self.print_2d_coords(endnode_position)
            
        # t = self.root_node.findData('time').value
        # if t >= TMAX:
            # self.root_node.getRootContext().animate = False
            # self.rec_socket.stop()
            # print('closing receive socket.')

    # def set_endnode_y_position(self, data):
        # """ Runs when new data is received from  a send socket.
            # Sets the y-position of the final node to the value
            # received from the send socket.
        # """
        # new_y_value = float(data['data'])
        
        # endnode_index = self.num_nodes - 1
        
        # endnode_desired_position = self.get_node_position(endnode_index)
        # endnode_desired_position[1] = new_y_value
        
        # self.set_position_at_index(endnode_index, endnode_desired_position)
        
        # endnode_new_position = self.get_node_position(endnode_index)
        # self.print_2d_coords(endnode_new_position)
        
    # def get_node_position(self, n):
        # """ Returns current xyz position of the node n."""
        # self.update_positions()
        # return self.positions[n]
        
    # def update_positions(self):
        # """ Updates the positions vector (all nodes) from the pointer."""
        # self.positions = self.positions_obj.value
        
    # def set_position_at_index(self, n, new_position):   
        # """ Sets the position of node n to new_position."""
        # # get positions as string
        # vs = self.positions_obj.getValueString()
        
        # # convert to numeric array
        # num_array = [float(i) for i in vs.split()]
        
        # # replace only the positions of node n
        # num_array[n*3] = new_position[0]
        # num_array[n*3 + 1] = new_position[1]
        # num_array[n*3 + 2] = new_position[2]
        
        # # revert to string and set as new position
        # vs_new = ' '.join([str(i) for i in num_array])
        # self.positions_obj.setValueString(vs_new)
        
    # def print_2d_coords(self, node_position):
        # """ Prints the time, as well as x- and y-coordinates
            # of the given node position."""
        # x = node_position[0]
        # y = node_position[1]
        # t = self.root_node.findData('time').value
        # print(f't:{t:2.2f} \t x = {x:2.2f}, y = {y:2.2f}')

def add_required_plugins():
    # PluginRepository.addFirstPath(SOFA_INSTALL_DIR)
    SofaRuntime.importPlugin("SofaComponentAll")
    SofaRuntime.importPlugin("SofaPython3")
    SofaRuntime.importPlugin("SofaOpenglVisual")

def main():
    add_required_plugins()
    root = Sofa.Core.Node("root")
    create_scene(root)
    
    print("Initialising simulation...")
    Sofa.Simulation.init(root)
    for i in range(4):
        Sofa.Simulation.animate(root, root.dt.value)
    
    if VERBOSE:
        Sofa.Simulation.print(root)
    
if __name__ == '__main__':
    main()
    