# Available at setup time due to pyproject.toml
import os

from pybind11.setup_helpers import Pybind11Extension, build_ext
from setuptools import setup

# get version from pyproject.toml to pass in to build macro
with open(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "pyproject.toml"))
) as f:
    __version__ = next(L.split("=")[1].strip().strip('"') for L in f if "version" in L)


# The main interface is through Pybind11Extension.
# * You can add cxx_std=11/14/17, and then build_ext can be removed.
# * You can set include_pybind11=false to add the include directory yourself,
#   say from a submodule.

setup(
    ext_modules=[
        Pybind11Extension(
            "vhacdx",
            ["src/vhacdx/main.cpp"],
            # Example: passing in the version to the compiled code
            define_macros=[("VERSION_INFO", __version__)],
        ),
    ],
    cmdclass={"build_ext": build_ext},
)
