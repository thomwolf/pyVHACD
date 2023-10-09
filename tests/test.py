import numpy as np
import vhacdx as pv

points = np.array(
    [
        [-0.5, -0.5, -0.5],
        [-0.5, -0.5, 0.5],
        [-0.5, 0.5, 0.5],
        [-0.5, 0.5, -0.5],
        [0.5, -0.5, -0.5],
        [0.5, 0.5, -0.5],
        [0.5, 0.5, 0.5],
        [0.5, -0.5, 0.5],
    ],
    dtype=np.float32,
)

faces = np.array(
    [
        3,
        0,
        1,
        3,
        3,
        2,
        3,
        1,
        3,
        4,
        5,
        7,
        3,
        6,
        7,
        5,
        3,
        0,
        4,
        1,
        3,
        7,
        1,
        4,
        3,
        3,
        2,
        5,
        3,
        6,
        5,
        2,
        3,
        0,
        3,
        4,
        3,
        5,
        4,
        3,
        3,
        1,
        7,
        2,
        3,
        6,
        2,
        7,
    ],
    dtype=np.int64,
)

output = pv.compute_vhacd(points, faces)

# check that the version is a string and roughly semantic-version
assert pv.__version__.count(".") == 2
assert isinstance(output, list)
assert len(output) == 1
assert len(output[0]) == 2
assert isinstance(output[0][0], np.ndarray)
assert isinstance(output[0][1], np.ndarray)
assert output[0][0].shape == (8, 3)
assert output[0][1].shape == (48,)
