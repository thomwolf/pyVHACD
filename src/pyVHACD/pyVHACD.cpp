#include <iostream>
#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>
#define ENABLE_VHACD_IMPLEMENTATION 1
#define VHACD_DISABLE_THREADING 0
#include "VHACD.h"

namespace py = pybind11;

/* C++ function that redirects to C func */
void compute_vhacd(py::array_t<double> points, py::array_t<int64_t> faces) {

	/*  read input arrays buffer_info */
	auto buf_points = points.request();
	auto buf_faces = faces.request();

	/*  variables */
	double *ptr_points = (double *) buf_points.ptr;
	int64_t *ptr_faces = (int64_t *) buf_faces.ptr;
	size_t num_points = buf_points.shape[0];
	size_t num_faces = buf_faces.shape[0] / 4;
	size_t num_triangle_indices = num_faces * 3;

	u_int32_t *triangles = new uint32_t[num_triangle_indices];
	for (uint32_t i=0; i<num_faces; i++)
	{
		// We skip the first index of the face array, which is the number of vertices in the face
		triangles[3*i] = ptr_faces[4*i+1];
		triangles[3*i+1] = ptr_faces[4*i+2];
		triangles[3*i+2] = ptr_faces[4*i+3];
	}

	VHACD::IVHACD::Parameters p;

#if VHACD_DISABLE_THREADING
	VHACD::IVHACD *iface = VHACD::CreateVHACD();
#else
	VHACD::IVHACD *iface = p.m_asyncACD ? VHACD::CreateVHACD_ASYNC() : VHACD::CreateVHACD();
#endif

	iface->Compute(ptr_points, num_points, triangles, num_faces, p);

	// // C code call 
	// loop_array(ptr1, (int)N);
}


/* Wrapping routines with PyBind */
PYBIND11_MODULE(wrapper, m) {
	    m.doc() = ""; // optional module docstring
	    m.def("compute_vhacd", &compute_vhacd, "Compute convex hulls");
}

