import pymesh
import numpy as np

def extractFeature():
    print("Glaucoma:")

    # Glaucoma
    meshHeights = []
    for i in range(0, 172):
        if i == 18:
            continue
        mesh = pymesh.load_mesh("output_glaucoma/glaucoma" + str(i).zfill(3) + ".obj")
        yMax = np.array(mesh.vertices)[:, 1].max()
        yMin = np.array(mesh.vertices)[:, 1].min()
        height = (yMax - yMin).round(6)
        meshHeights.append(height)

    meshWidths = []
    for i in range(0, 172):
        if i == 18:
            continue
        mesh = pymesh.load_mesh("output_glaucoma/glaucoma" + str(i).zfill(3) + ".obj")
        xMax = np.array(mesh.vertices)[:, 0].max()
        xMin = np.array(mesh.vertices)[:, 0].min()
        width = (xMax - xMin).round(6)
        meshWidths.append(width)

    meshDepths = []
    for i in range(0, 172):
        if i == 18:
            continue
        mesh = pymesh.load_mesh("output_glaucoma/glaucoma" + str(i).zfill(3) + ".obj")
        zMax = np.array(mesh.vertices)[:, 2].max()
        zMin = np.array(mesh.vertices)[:, 2].min()
        depth = (zMax - zMin).round(6)
        meshDepths.append(depth)

    volumes = []
    for i in range(0, 171):
        if i == 18:
            volumes.append(0)

        volumes.append(round((meshHeights[i] * meshWidths[i] * meshDepths[i]), 6))

    volumes[18] = np.array(volumes).mean().round(6)
    for i in range(0, 172):
        print(str(volumes[i]))

    print("Normal:")

    # Normal
    meshHeights = []
    for i in range(0, 313):
        mesh = pymesh.load_mesh("output_normal/normal" + str(i).zfill(3) + ".obj")
        yMax = np.array(mesh.vertices)[:, 1].max()
        yMin = np.array(mesh.vertices)[:, 1].min()
        height = (yMax - yMin).round(6)
        meshHeights.append(height)

    meshWidths = []
    for i in range(0, 313):
        mesh = pymesh.load_mesh("output_normal/normal" + str(i).zfill(3) + ".obj")
        xMax = np.array(mesh.vertices)[:, 0].max()
        xMin = np.array(mesh.vertices)[:, 0].min()
        width = (xMax - xMin).round(6)
        meshWidths.append(width)

    meshDepths = []
    for i in range(0, 313):
        mesh = pymesh.load_mesh("output_normal/normal" + str(i).zfill(3) + ".obj")
        zMax = np.array(mesh.vertices)[:, 2].max()
        zMin = np.array(mesh.vertices)[:, 2].min()
        depth = (zMax - zMin).round(6)
        meshDepths.append(depth)

    volumes = []
    for i in range(0, 313):
        volumes.append(round((meshHeights[i] * meshWidths[i] * meshDepths[i]), 6))

    for i in range(0, 313):
        print(str(volumes[i]))
    
    return

