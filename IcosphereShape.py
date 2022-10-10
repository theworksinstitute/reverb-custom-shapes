try:
	import nap  # noqa
except ModuleNotFoundError:
	import shapes.utils as nap
from shapes.utils import read_vertices_from_file


def getPositions(resolution, hollow): # noqa
	icosphere_resolutions = [12, 42, 92, 162, 252, 362, 492, 642, 812, 1002, 1212, 1442, 1692, 1962, 2252]
	vertices_count = next(i for i in icosphere_resolutions if resolution <= i)
	positions = []
	vertices = read_vertices_from_file(f'shapes/icosphere/coordinates_{vertices_count}.txt')

	for v in vertices: # noqa
		positions.append(nap.vec3(v[0], v[1], v[2]))

	return positions


def getVisualizationVertices():
	return []


def getVisualizationEdges():
	return []


if __name__ == '__main__':
	from shapes.window import show_window
	show_window(getPositions(500, 0))
