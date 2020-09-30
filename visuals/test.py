import SofaRuntime
from SofaRuntime import PluginRepository

import Sofa
import Sofa.Gui
import Sofa.Simulation

import Sofa.Core
from Sofa.constants import *
from random import randint
from splib.animation import easing
import math
import numpy

SOFA_INSTALL_DIR = "/home/user3/sofa/build2/install"

def add_required_plugins():
    PluginRepository.addFirstPath(SOFA_INSTALL_DIR)
    SofaRuntime.importPlugin("SofaComponentAll")
    SofaRuntime.importPlugin("SofaPython3")
    SofaRuntime.importPlugin("SofaOpenglVisual")

def Sphere(rootNode, name, position, color):
    #Creating the sphere
    sphere = rootNode.addChild(name)
    sphere.addObject('MechanicalObject', name="mstate", template="Rigid3", position=position)

    #### Visualization of the sphere
    sphereVisu = sphere.addChild("VisualModel")
    sphereVisu.loader = sphereVisu.addObject('MeshObjLoader', name="loader", 
        filename="./mesh/ball.obj", scale=0.5)
    sphereVisu.addObject('OglModel', name="model", src="@loader", color=color)
    sphereVisu.addObject('RigidMapping')
    return sphere

def createScene(rootNode):
    """ This scene is an example scene to demonstrate an implementation of a Controller for the Camera in runSofa. 
        To test this, in runSofa, you must put the View parameter (top left of the runSofa window) to OpenGL
        Then click on Animate, and move the Camera using Ctrl + z, q, d and x, orientate it by clicking and moving with the Mouse!
    """
    for i in range(10):
        sphere = Sphere(rootNode, "sphere"+str(i), [randint(0,6),randint(0,6),randint(0,6),0,0,0,1],[i/40.0,i*0.7/40.0,0.9])
    return rootNode
    
def main():
    add_required_plugins()
    root = Sofa.Core.Node("root")
    createScene(root)
    Sofa.Simulation.init(root)
        
    Sofa.Gui.GUIManager.Init("simple_scene", "qglviewer")
    Sofa.Gui.GUIManager.createGUI(root)
    Sofa.Gui.GUIManager.MainLoop(root)
    
if __name__ == '__main__':
    main()
