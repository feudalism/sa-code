import SofaRuntime
import Sofa
import Sofa.Gui

SOFA_INSTALL_DIR = "/home/user3/sofa/build2/install"

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
    
def createScene(root):
    pass
    
def launch_gui(root):
    # Simulation initialisation required for loading gui
    Sofa.Simulation.init(root)
    
    Sofa.Gui.GUIManager.Init("simple_scene", "qglviewer")
    Sofa.Gui.GUIManager.createGUI(root)
    Sofa.Gui.GUIManager.MainLoop(root)
    Sofa.Gui.GUIManager.closeGUI()
    
add_required_plugins()
root = make_root()
createScene(root)
launch_gui(root)