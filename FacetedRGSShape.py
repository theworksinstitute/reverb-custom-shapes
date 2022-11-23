try:
	import nap  # noqa
except ModuleNotFoundError:
	import shapes.utils as nap
from shapes import utils

def getPositions(resolution, hollow): # noqa
	if resolution != 1:
		vertices = utils.dummy_shape()
	else:
		vertices = utils.read_vertices_from_file('shapes/RGS_1_faceted/coordinates.txt')

	positions = []  # noqa
	for v in vertices:
		positions.append(nap.vec3(v[0]/2, v[2]/2, v[1]/2))
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
