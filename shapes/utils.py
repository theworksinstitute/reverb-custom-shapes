import re
import os


def read_vertices_from_file(path):
	if 'data' in os.getcwd():
		path = os.path.join(os.getcwd(), 'scripts/reverb-custom-shapes', path)
	with open(path, 'r') as file:
		contents = file.readlines()
		return list(map(convert_line_to_list, contents))


def convert_line_to_list(file_line):
	values = re.search(r'{(.+), (.+), (.+)}', file_line).groups()
	return list(map(float, values))


def vec3(a, b, c):
	return a, b, c
