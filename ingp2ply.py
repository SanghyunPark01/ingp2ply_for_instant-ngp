resolution = 350
ingp_path = "../data/nerf/fox/transforms_base.ingp"
output_ply_name = "ingp2ply_output.ply"

#--------------------------------------------------
pyngp_path = '../build'
import sys
sys.path.append(pyngp_path)
import pyngp as ngp
import numpy as np
from plyfile import PlyData, PlyElement

def round_up_to_base(x, base=10):
    return x + (base - x) % base

def get_marching_cubes_res(res_1d: int, aabb:  ngp.BoundingBox ) -> np.ndarray:
	scale = res_1d / (aabb.max - aabb.min).max()
	res3d = (aabb.max - aabb.min) * scale + 0.5
	res3d = round_up_to_base(res3d.astype(np.int32), 16)
	return res3d

mode = ngp.TestbedMode.Nerf
testbed = ngp.Testbed(mode)
testbed.load_snapshot(ingp_path)
#mc = testbed.compute_marching_cubes_mesh()
mc = testbed.compute_marching_cubes_mesh(resolution=get_marching_cubes_res(resolution, testbed.aabb), aabb=testbed.aabb, thresh=2)
vertex = np.array(list(zip(*mc["V"].T)), dtype=[('x', 'f4'), ('y', 'f4'), ('z', 'f4')])
vertex_color = np.array(list(zip(*((mc["C"] * 255).T))), dtype=[('red', 'u1'), ('green', 'u1'), ('blue', 'u1')])

n = len(vertex)
assert len(vertex_color) == n

vertex_all = np.empty(n, vertex.dtype.descr + vertex_color.dtype.descr)

for prop in vertex.dtype.names:
    vertex_all[prop] = vertex[prop]

for prop in vertex_color.dtype.names:
    vertex_all[prop] = vertex_color[prop]

ply = PlyData([PlyElement.describe(vertex_all, 'vertex')], text=False)

ply.write(output_ply_name)