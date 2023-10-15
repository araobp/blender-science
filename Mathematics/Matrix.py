import bpy

CUBE_SIZE = 0.9
PADDING = 0.1

def add_collection(name, parent=None):
    collection = bpy.data.collections.new(name)
    if parent is None:
        bpy.context.scene.collection.children.link(collection)
    else:
        parent.children.link(collection)
    return collection

parent = None

for collection in bpy.data.collections:
    if collection.name == 'MFSCs':
        parent = collection
        break

if parent is None:
    parent = add_collection('MFSCs')

def add_cube(x_start, x_end):
    for x in range(x_start, x_end):
        xx = x * (CUBE_SIZE + PADDING)
        for z in range(0,40):
            zz = z * (CUBE_SIZE + PADDING)
            bpy.ops.mesh.primitive_cube_add(location=(xx,0,zz), size=1, scale=(CUBE_SIZE, CUBE_SIZE, CUBE_SIZE))
            cube = bpy.context.selected_objects[0]
            cube.name = 'C-{}-{}'.format(x, z)
            old_col = cube.users_collection
            parent.objects.link(cube)
            for ob in old_col:
                ob.objects.unlink(cube)

### It takes a lot of time to generate cubes ###

#add_cube(0,10)
#add_cube(10,20)
#add_cube(20,30)
#add_cube(30,40)
#add_cube(40,50)
#add_cube(50,60)
#add_cube(60,70)
#add_cube(70,80)
#add_cube(80,90)
#add_cube(90,100)
#add_cube(100,110)
#add_cube(110,120)
#add_cube(120,130)
#add_cube(130,140)
#add_cube(140,150)
#add_cube(150,160)
#add_cube(160,170)
#add_cube(170,180)
#add_cube(180,190)
#add_cube(190,200)


            
        