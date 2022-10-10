#!/usr/bin/env python3

from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import
from matplotlib import pyplot as plt
import matplotlib.animation

import config
from E8 import E8
import numpy as np

e8 = E8()


def update_graph(num):
	e8.current_time = num/10
	plot_data = np.array(e8.get_matrix())
	graph.set_data(plot_data[:, 0], plot_data[:, 1])
	graph.set_3d_properties(plot_data[:, 2])
	# maximum_value = max(list(map(lambda x: abs(x), plot_data.flatten())))
	# title.set_text('3D Test, time={}'.format(num))
	return title, graph,


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.autoscale_view()
axis_limit = config.axis_limit
ax.set_xlim3d(-1*axis_limit, axis_limit)
ax.set_ylim3d(-1*axis_limit, axis_limit)
ax.set_zlim3d(-1*axis_limit, axis_limit)
title = ax.set_title('3D Test')

data = np.array(e8.get_matrix())
graph, = ax.plot(data[:, 0], data[:, 1], data[:, 2], linestyle="", marker="o")

ani = matplotlib.animation.FuncAnimation(fig, update_graph,
							   interval=config.update_interval, blit=True)

plt.show()
