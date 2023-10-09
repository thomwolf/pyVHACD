# vhacdx
Python bindings for V-HACD

A very simple and raw python binding for [V-HACD](https://github.com/kmammou/v-hacd) that is forked from [thomwolf/pyVHACD](https://github.com/thomwolf/pyVHACD) which generates an approximate convex decomposition of a triangle mesh.

Contains a single method: `output = compute_vhacd(points, faces)` which take as inputs:
- points: a (N, 3) Numpy array of double containing the coordinates of the N vertex of the mesh
- face: a (M,) Numpy array of uint32 containing the face vertxe indices were M is 3 times the number of faces

Gives as output a list (number of convex hulls) of pairs of points-faces for each convex hull.

# To install
```
pip install vhacdx
```
