import numpy as np

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt  # noqa

resolution = 1  # TODO


def show_window(positions):
	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')
	data = np.array(positions)
	ax.plot(data[:, 0], data[:, 1], data[:, 2], linestyle="", marker="o")
	plt.show()
