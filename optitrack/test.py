import SofaRuntime
import Sofa
import Sofa.Gui

SOFA_INSTALL_DIR = "/home/user3/sofa/build2/install"

from BeamMin import BeamMin as Beam

def add_required_plugins():
    SofaRuntime.PluginRepository.addFirstPath(SOFA_INSTALL_DIR)
    SofaRuntime.importPlugin("SofaComponentAll")
    SofaRuntime.importPlugin("SofaPython3")
    SofaRuntime.importPlugin("SofaOpenglVisual")
    SofaRuntime.importPlugin("OptiTrackNatNet")
    
def make_root():
    root = Sofa.Core.Node("root")
    
    # simulation settings
    root.gravity = [0, 0., 0]
    root.dt = 1
    
    return root
    
def create_otnn_client(node):
    # OptiTrack client
    otnn_client = node.addObject('OptiTrackNatNetClient',
        name='otnnClient',
        clientName='127.0.0.1',
        serverName='127.0.0.1')
    otnn_client.init()
    # print(otnn_client.recv_data_packet) # not available
    
    return otnn_client

def create_otnn_device(node, client):
    device = node.addObject('OptiTrackNatNetDevice',
        name='HeadDevice',
        trackableName='Head',   # NatNet
        isGlobalFrame='1',      # consider this the global frame
        inMarkersMeshFile="./data/markers-Head.obj",
        simMarkersMeshFile="./data/markers-Head.obj",
        drawMarkersColor="0 1 0 1",
        drawAxisSize="50 10 50",
        drawMarkersSize="2",
        natNetClient=client, # Warning: Could not read value for link natNetClient
        )
    return device
        
def create_head(root):
    head_node = root.addChild('head')
    
    client = create_otnn_client(head_node)
    device = create_otnn_device(head_node, client)
    
    head_visu_node = head_node.addChild('head_visu')
    head_visu_node.addObject('OglModel',
        name="vm",
        filename="./data/head_low.obj"
        )
        
    return head_node, client, device
    
def createScene(root):
    # object to be modelled: beam
    beam = Beam(root, 'deformableBeam')
    head, _, device = create_head(root)
    
    print('---------')
    print(device)
    print(dir(device))
     
    # visuals
    root.addObject('VisualStyle',
        displayFlags='showVisual showWireframe showBehaviorModels')
    
    return root
    
def launch_gui(root):
    # Simulation initialisation required for loading gui
    Sofa.Simulation.init(root)
    
    Sofa.Gui.GUIManager.Init("simple_scene", "qglviewer")
    Sofa.Gui.GUIManager.createGUI(root)
    Sofa.Gui.GUIManager.MainLoop(root)
    Sofa.Gui.GUIManager.closeGUI()
    
def main():
    add_required_plugins()
    root = make_root()
    createScene(root)
    # launch_gui(root)
    
if __name__ == '__main__':
    main()