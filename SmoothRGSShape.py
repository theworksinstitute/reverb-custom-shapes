try:
	import nap  # noqa
except ModuleNotFoundError:
	import shapes.utils as nap
from shapes.utils import read_vertices_from_file


def getPositions(resolution, hollow): # noqa
	vertices = read_vertices_from_file('shapes/RGS_1_smooth/coordinates.txt')

	positions = [] # noqa

	for v in vertices:
		positions.append(nap.vec3(v[0], v[1], v[2]))

	if resolution != 1:
		for i in range(1, 3):
			for v in vertices:
				positions.append(nap.vec3(v[0]+10*i, v[1], v[2]))
	return positions


def getVisualizationVertices():
	return []


# # ___getVisualizaitonEdges function___
# # If you want your shape to be visualised, return the edges here as a list of pairs of indices.
def getVisualizationEdges():
	return []


if __name__ == '__main__':
	from shapes.window import show_window
	show_window(getPositions(2, 0))
