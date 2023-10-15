import bpy
import numpy as np
import matplotlib.pyplot as plt

# Get colormap data from matplotlib
MATPLOTLIB_COLORMAPS = ['ocean', 'viridis', 'hot', 'gray', 'magma', 'cubehelix',\
'BrBG', 'RdBu', 'bwr', 'coolwarm', 'seismic']

# CAUTION! This block clears all the materials!
def clearAll():
    for material in bpy.data.materials:
        material.user_clear()
        bpy.data.materials.remove(material)

def createColorMap(matplotlib_colormap):
    # Create materials of matplotlib colormap (Total number of mateials is 256 for each)
    cmap = plt.get_cmap(matplotlib_colormap)
    rgba_array = np.array([cmap(i) for i in range(cmap.N)])
    
    for i in range(rgba_array.shape[0]):
        mat = bpy.data.materials.new(name="{}-{}".format(matplotlib_colormap, i))
        mat.diffuse_color = rgba_array[i]
        mat.use_nodes = True
        mat.use_screen_refraction = True
        mat.use_fake_user = True
        for n in mat.node_tree.nodes:
            if n.type == 'BSDF_PRINCIPLED':
                n.inputs["Base Color"].default_value = rgba_array[i]
                n.inputs["Metallic"].default_value = 0.0                
                n.inputs["Roughness"].default_value = 0.0
                n.inputs["Transmission"].default_value = 0.5
                n.inputs["Emission Strength"].default_value = 1.0
                n.inputs["Clearcoat"].default_value = 1.0
                n.inputs["Emission"].default_value = rgba_array[i]

clearAll()

for colormap in MATPLOTLIB_COLORMAPS:
    createColorMap(colormap)