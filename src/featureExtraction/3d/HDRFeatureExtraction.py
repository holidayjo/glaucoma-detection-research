import pymesh
import numpy as np

def extractFeature():
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

    meshDepths = []
    for i in range(0, 172):
        if i == 18:
            continue
        mesh = pymesh.load_mesh("output_glaucoma/glaucoma" + str(i).zfill(3) + ".obj")
        zMax = np.array(mesh.vertices)[:, 2].max()
        zMin = np.array(mesh.vertices)[:, 2].min()
        depth = (zMax - zMin).round(6)
        meshDepths.append(depth)

    hdrs = []
    for i in range(0, 171):
        if i == 18:
            hdrs.append(0)
        if (meshDepths[i] == 0):
            hdrs.append(0)
        else:
            hdrs.append(round((meshHeights[i] / meshDepths[i]), 6))
        print("hdrs[" + str(i) + "] = " + str(hdrs[i]) + ";")

    hdrs[18] = np.array(hdrs).mean().round(6)
    for i in range(0, 172):
        print(str(hdrs[i]))

    # Normal
    meshHeights = []
    for i in range(0, 313):
        mesh = pymesh.load_mesh("output_normal/normal" + str(i).zfill(3) + ".obj")
        yMax = np.array(mesh.vertices)[:, 1].max()
        yMin = np.array(mesh.vertices)[:, 1].min()
        height = (yMax - yMin).round(6)
        meshHeights.append(height)

    meshDepths = []
    for i in range(0, 313):
        mesh = pymesh.load_mesh("output_normal/normal" + str(i).zfill(3) + ".obj")
        zMax = np.array(mesh.vertices)[:, 2].max()
        zMin = np.array(mesh.vertices)[:, 2].min()
        depth = (zMax - zMin).round(6)
        meshDepths.append(depth)

    hdrs = []
    for i in range(0, 313):
        if (meshDepths[i] == 0):
            hdrs.append(0)
        else:
            hdrs.append(round((meshHeights[i] / meshDepths[i]), 6))
        print("hdrs[" + str(i) + "] = " + str(hdrs[i]) + ";")

    for i in range(0, 313):
        print(str(hdrs[i]))
    
    return

