import SofaRuntime
import Sofa
import Sofa.Gui
import Sofa.Core
print(dir(Sofa.Core))
print(dir(Sofa.Core.Data))

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
    client = node.addObject('OptiTrackNatNetClient',        # Sofa.Core.Object
        name='otnnClient',
        clientName='127.0.0.1',
        serverName='127.0.0.1',
        scale='1000',
        drawOtherMarkersSize='2',   # unknown markers
        drawTrackedMarkersSize='1') # known markers
    client.init()
    return client

def create_otnn_device(node, client, mesh_path):
    device = node.addObject('OptiTrackNatNetDevice',
        name='HeadDevice',
        trackableName='Head',   # NatNet
        isGlobalFrame='1',      # consider this the global frame
        # inMarkersMeshFile="./data/markers-Head.obj",
        # simMarkersMeshFile="./data/markers-Head.obj",
        # inMarkersMeshFile=mesh_path,
        # simMarkersMeshFile="@../grid",
        drawMarkersColor="0 1 0 1",
        drawAxisSize="50 10 50",
        drawMarkersSize="2",
        # natNetClient=client, # Warning: Could not read value for link natNetClient
        )
    device.init()
    return device
    
def create_beam(root):
    beam = Beam(root, 'deformableBeam')
    main_node = beam.main_node # RegularGrid
    mesh_path = beam.grid_path
    
    client = create_otnn_client(main_node)
    device = create_otnn_device(main_node, client, mesh_path)
    
    return beam, client, device
    
def createScene(root):
    # object to be modelled: beam
    create_beam(root)
     
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
    root = make_root()
    createScene(root)
    # launch_gui(root)
    
    

# ------run-------
add_required_plugins()
if __name__ == '__main__':
    main()
    
    