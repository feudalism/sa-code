# import os, sys, time

from settings import PORT, TMAX, VERBOSE, SOFA_INSTALL_DIR

import SofaRuntime
import Sofa
from SofaRuntime import PluginRepository

from PositionController import PositionController
from BeamMin import BeamMin as Beam

# import Sofa.Gui
# from DataSocket import TCPReceiveSocket

def create_scene(root_node):
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

def add_required_plugins():
    # PluginRepository.addFirstPath(SOFA_INSTALL_DIR)
    SofaRuntime.importPlugin("SofaComponentAll")
    SofaRuntime.importPlugin("SofaPython3")
    SofaRuntime.importPlugin("SofaOpenglVisual")

def animate(root):
    print("Initialising simulation...")
    Sofa.Simulation.init(root)
    # for i in range(4):
        # Sofa.Simulation.animate(root, root.dt.value)    

def main():
    add_required_plugins()
    root = Sofa.Core.Node("root")
    create_scene(root)
    animate(root)
    
    if VERBOSE:
        Sofa.Simulation.print(root)
    
if __name__ == '__main__':
    main()
    