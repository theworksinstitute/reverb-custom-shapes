try:
	import nap  # noqa
except ModuleNotFoundError:
	import shapes.utils as nap
from shapes import utils


def getPositions(resolution, hollow): # noqa
	if resolution != 1:
		vertices = utils.dummy_shape()
	else:
		vertices = utils.read_vertices_from_file('shapes/e8/coordinates.txt')

	positions = []  # noqa
	for v in vertices:
		positions.append(nap.vec3(v[0], v[1], v[2]))
	return positions


def getVisualizationVertices():
	return []


def getVisualizationEdges():
	return []


if __name__ == '__main__':
	from shapes.window import show_window
	show_window(getPositions(1, 0))
