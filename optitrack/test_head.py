import SofaRuntime
import Sofa
import Sofa.Gui

SOFA_INSTALL_DIR = "/home/user3/sofa/build2/install"

from OTController import OTController

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
    client = node.addObject('OptiTrackNatNetClient',
        name='otnnClient',
        # serverName='169.254.165.78')
        serverName='localhost:4000')
    client.init()
    
    return client

def create_otnn_device(node, name, track_name, mesh_file, client, global_frame=None):
    # [WIP] for generalising create device
            
    device = node.addObject('OptiTrackNatNetDevice',
        name=name,
        trackableName=track_name,   # NatNet
        # isGlobalFrame = glob,
        # inMarkersMeshFile=mesh_file,
        # simMarkersMeshFile=mesh_file,
        drawMarkersColor="0 1 0 1",
        drawAxisSize="50 10 50",
        drawMarkersSize="2",
        # natNetClient=client, # Warning: Could not read value for link natNetClient
        )
        
    if global_frame is None:
        # device.isGlobalFrame.value = '1' # RuntimeError: Unable to cast Python instance to C++ type
        with device.isGlobalFrame.writeableArray() as value: # [0]
            value[0]=1      # consider this the global frame
    # else:
        # device.isGlobalFrame='0'      
        # device.inGlobalFrame=global_frame
        
    device.init()
        
    return device
        
def create_head(root, otnn_client):
    head = root.addChild('head')
    
    # otnn device
    mesh_file = './data/markers-Head.obj' 
    otnn_device = head.addObject('OptiTrackNatNetDevice',
        name='HeadDevice',
        trackableName='Head',   # NatNet
        isGlobalFrame = '1',
        inMarkersMeshFile=mesh_file,
        simMarkersMeshFile=mesh_file,
        drawMarkersColor="0 1 0 1",
        drawAxisSize="50 10 50",
        drawMarkersSize="2",
        # natNetClient=client, # Warning: Could not read value for link natNetClient
        )
    otnn_device.init()
    
    # visual
    head_visu_node = head.addChild('head_visu')
    head_visu_node.addObject('OglModel',
        name="vm",
        filename="./data/head_low.obj"
        )
        
    return head, otnn_device
    
def create_cystitome(root, otnn_client):
    cystitome = root.addChild('cystitome')
    
    # mech
    cystitome.addObject('MechanicalObject',
        name='msl',
        template='Rigid3d')
    
    # otnn device
    mesh_file = './data/markers-Cystitome.obj' 
    otnn_device = cystitome.addObject('OptiTrackNatNetDevice',
        name='CutDevice',
        trackableName='Cut',   # NatNet
        inGlobalFrame = '@../head/HeadDevice.frame',
        inMarkersMeshFile=mesh_file,
        simMarkersMeshFile=mesh_file,
        controlNode='1',
        drawMarkersColor="1 0 1 1",
        drawAxisSize="10 10 10",
        drawMarkersSize="2",
        # natNetClient=client, # Warning: Could not read value for link natNetClient
        )
    otnn_device.init()
        
    # cut edges
    cut_edges = cystitome.addChild('CutEdges')
    cut_edges.addObject('MeshTopology',
        name='cutEdges',
        position="0 0.0167 -0.0424 0 0.1959 0.2303",
        edges="0 1"
        )
        
    # surface
    cystitome.addChild('Surface')
    
        
    # visual
    ct_visu_node = cystitome.addChild('ct_visu')
    ct_visu_node.addObject('OglModel',
        name="ctvm",
        filename="./data/cystitome.obj"
        )
    
def createScene(root):
    # ot controller - does nothing so far
    # ot_controller = OTController(name="ot_controller",
                            # root=root)

    # otnn client
    otnn_client = create_otnn_client(root)

    # object to be modelled: head
    create_head(root, otnn_client)
    create_cystitome(root, otnn_client)
     
    # visuals -- wireframe
    root.addObject('VisualStyle',
        displayFlags='showVisual showWireframe showBehaviorModels')
    
    print('--------------done')
    
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
    launch_gui(root)
    
if __name__ == '__main__':
    main()