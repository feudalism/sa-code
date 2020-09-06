class BeamMin():
    """ A minimal 2D beam object in SOFA. """
    
    def __init__(self, root, name):
        self.root_node = root
        self.main_node = root.createChild(name)
        self.mech_obj = None  
             
        # structure
        self.main_node.createObject(
            'RegularGrid',
            name='grid',
            n=[5, 2, 1],     # 4 grids in x, ...
            min=[0., 0., 0.], # min pos of object
            max=[4., 1., 0.]  # max pos of object
            )
        
        # mechanical obj
        self.mech_obj = self.main_node.createObject(
            'MechanicalObject',
            name='DOFs')
        self.main_node.createObject('UniformMass',
            name='mass',
            totalMass=10)
        # maybe better off in a child node (contact node?)
        self.main_node.createObject('StiffSpringForceField',
            name='ff',
            stiffness='1E6',
            length=1)
        # self.main_node.createObject('LinearMapping', template='Affine,Vec3d')
        
        # visuals
        self.visu_node = self.main_node.createChild('visual')
        self.visu_node.createObject(
            'OglModel', # uses SofaOpenglVisual, displays graphics
            template='Vec3d',
            name='visual',
            src='@../grid',
            color='0.8 0.2 0.2 1')
        self.visu_node.createObject('IdentityMapping',
            template='Vec3d,Vec3d') # update animation with the simulation results