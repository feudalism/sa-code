# import os, sys, time

from settings import PORT, TMAX, VERBOSE, SOFA_INSTALL_DIR, NUMBER_OF_MESSAGES
from threading import Thread

import SofaRuntime
from SofaRuntime import PluginRepository
import Sofa
import Sofa.Gui

from PositionController import PositionController
from BeamMin import BeamMin as Beam

from DataSocket import TCPSendSocket, NUMPY
import time

def createScene(root_node):
    # object to be modelled: beam
    beam = Beam(root_node, 'deformableBeam')
    
    # controller
    pos_controller = PositionController(name="pos_controller",
                            root_node=root_node,
                            model=beam)
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
    
    return root_node

def add_required_plugins():
    PluginRepository.addFirstPath(SOFA_INSTALL_DIR)
    SofaRuntime.importPlugin("SofaComponentAll")
    SofaRuntime.importPlugin("SofaPython3")
    SofaRuntime.importPlugin("SofaOpenglVisual")

def animate(root):
    print("Initialising simulation...")
    Sofa.Simulation.init(root)
    
    Sofa.Gui.GUIManager.Init("simple_scene", "qglviewer")
    Sofa.Gui.GUIManager.createGUI(root)
    Sofa.Gui.GUIManager.MainLoop(root)
    Sofa.Gui.GUIManager.closeGUI()
    
    # t = root.time.value
    # while t < TMAX:
        # Sofa.Simulation.animate(root, root.dt.value)    
        # t = root.time.value
    
def sending_function():
    """ Creates a send socket to transmit sample data. """
    send_socket = TCPSendSocket(tcp_port=PORT, send_type=NUMPY)
    send_socket.start(blocking=True)

    # sample data: 1, 2, ... 6
    for i in range(NUMBER_OF_MESSAGES):
        print(f"\t sending! {i+1}")
        send_socket.send_data(i+1)
        time.sleep(1.5)

    print("closing send socket.")
    send_socket.stop()
    
def receiving_function():
    """ Runs SOFA with the Python script to change the y-position value
        of the end node of a beam.
        
        A receive socket is started from within the simulation
        once the graph is initialised.
        The y-position of the end node is given by the data received
        from the send socket.
    """    
    root = Sofa.Core.Node("root")
    createScene(root)
    
    if VERBOSE:
        Sofa.Simulation.print(root)
        print()
        
    animate(root)
    
def main():
    add_required_plugins()
    
    send_thread = Thread(target=sending_function)
    rec_thread = Thread(target=receiving_function)

    send_thread.start()
    rec_thread.start()

    send_thread.join()
    rec_thread.join()
    
if __name__ == '__main__':
    main()
    