import pymesh
import numpy as np

def extractFeature():
    print("Glaucoma:")

    # Glaucoma
    numFaces = []
    for i in range(0, 172):
        if i == 18:
            numFaces.append(0)
        else:
            mesh = pymesh.load_mesh("output_glaucoma/glaucoma" + str(i).zfill(3) + ".obj")
            numFaces.append(mesh.num_faces)

    numFaces[18] = int(np.array(numFaces).mean())
    for i in range(0, 172):
        print(str(numFaces[i]))

    print("Normal:")

    # Normal
    numFaces = []
    for i in range(0, 313):
        mesh = pymesh.load_mesh("output_normal/normal" + str(i).zfill(3) + ".obj")
        numFaces.append(mesh.num_faces)

    for i in range(0, 313):
        print(str(numFaces[i]))
    
    return

