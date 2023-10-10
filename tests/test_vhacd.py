import numpy as np
import vhacdx as pv


def test_basic():
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

    assert isinstance(output, list)
    assert len(output) == 1
    assert len(output[0]) == 2

    # expand the first result
    vertices, faces = output[0]

    # should be floating point ndarray
    assert isinstance(vertices, np.ndarray)
    assert vertices.dtype.kind == "f"

    # should be unsigned int ndarray
    assert isinstance(faces, np.ndarray)
    assert faces.dtype.kind == "u"

    assert vertices.shape == (8, 3)
    assert faces.shape == (12, 3)


def test_import():
    # check that the version is a string and roughly semantic-version
    assert pv.__version__.count(".") == 2


if __name__ == "__main__":
    test_basic()
    test_import()
