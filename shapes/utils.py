import re


def read_vertices_from_file(file_name):
	with open(file_name, 'r') as file:
		contents = file.readlines()
		return list(map(convert_line_to_list, contents))


def convert_line_to_list(file_line):
	values = re.search(r'{(.+), (.+), (.+)}', file_line).groups()
	return list(map(float, values))


def vec3(a, b, c):
	return a, b, c
