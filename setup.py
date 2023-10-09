# Available at setup time due to pyproject.toml
from pybind11.setup_helpers import Pybind11Extension, build_ext
from setuptools import setup

__version__ = "0.0.3"

# The main interface is through Pybind11Extension.
# * You can add cxx_std=11/14/17, and then build_ext can be removed.
# * You can set include_pybind11=false to add the include directory yourself,
#   say from a submodule.
#
# Note:
#   Sort input source files if you glob sources to ensure bit-for-bit
#   reproducible builds (https://github.com/pybind/python_example/pull/53)

ext_modules = [
    Pybind11Extension(
        "vhacdx",
        ["src/vhacdx/main.cpp"],
        # Example: passing in the version to the compiled code
        define_macros=[("VERSION_INFO", __version__)],
    ),
]

setup(
    name="vhacdx",
    version=__version__,
    author="Thomas Wolf",
    author_email="thomas@huggingface.co",
    url="https://github.com/trimesh/vhacdx",
    description="Python bindings for VHACD",
    long_description="Python bindings for VHACD",
    ext_modules=ext_modules,
    extras_require={"test": ["pytest", "numpy"]},
    install_requires=["pybind11>=2.2", "numpy"],
    cmdclass={"build_ext": build_ext},
    zip_safe=False,
    python_requires=">=3.6",
)
