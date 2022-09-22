# pyVHACD
Python bindings for V-HACD

A very simple and raw python binding for V-HACD (https://github.com/kmammou/v-hacd)

Generate a set of convex hulls for a triangulated mesh.

Contains a single method: `output = compute_vhacd(points, faces)` which take as inputs:
- points: a (N, 3) Numpy array of double containing the coordinates of the N vertex of the mesh
- face: a (M,) Numpy array of uint32 containing the face vertxe indices were M is 3 times the number of faces

Gives as output a list (number of convex hulls) of pairs of points-faces for each convex hull.

Examples usage with pyvista:
```
import pyvista
import pyVHACD

mesh = pyvista.examples.download_bunny().triangulate()

outputs = pyVHACD.compute_vhacd(mesh.points, mesh.faces)

plotter = pyvista.Plotter(window_size=(1500, 1100))
for i, (mesh_points, mesh_faces) in enumerate(outputs):
     plotter.add_mesh(pyvista.PolyData(mesh_points, mesh_faces), color=list(pyvista.hexcolors.keys())[i])

plotter.show()
```
