import pymesh
import numpy as np

# Glaucoma
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

wdrs = []
for i in range(0, 171):
    if i == 18:
        wdrs.append(0)
    if (meshDepths[i] == 0):
        wdrs.append(0)
    else:
        wdrs.append(round((meshWidths[i] / meshDepths[i]), 6))
    print("wdrs[" + str(i) + "] = " + str(wdrs[i]) + ";")

wdrs[18] = np.array(wdrs).mean().round(6)
for i in range(0, 172):
    print(str(wdrs[i]))

# Normal
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

wdrs = []
for i in range(0, 313):
    if (meshDepths[i] == 0):
        wdrs.append(0)
    else:
        wdrs.append(round((meshWidths[i] / meshDepths[i]), 6))
    print("wdrs[" + str(i) + "] = " + str(wdrs[i]) + ";")

for i in range(0, 313):
    print(str(wdrs[i]))