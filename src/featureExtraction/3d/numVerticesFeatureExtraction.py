import pymesh
import numpy as np

def extractFeature():
    print("Glaucoma:")

    # Glaucoma
    numVertices = []
    for i in range(0, 172):
        if i == 18:
            numVertices.append(0)
        else:
            mesh = pymesh.load_mesh("output_glaucoma/glaucoma" + str(i).zfill(3) + ".obj")
            numVertices.append(mesh.num_vertices)

    numVertices[18] = int(np.array(numVertices).mean())
    for i in range(0, 172):
        print(str(numVertices[i]))

    print("Normal:")

    # Normal
    numVertices = []
    for i in range(0, 313):
        mesh = pymesh.load_mesh("output_normal/normal" + str(i).zfill(3) + ".obj")
        numVertices.append(mesh.num_vertices)

    for i in range(0, 313):
        print(str(numVertices[i]))
    
    return

