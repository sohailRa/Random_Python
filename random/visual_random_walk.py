import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
	r_walk = RandomWalk()
	r_walk.walk()

	point_nums = list(range(r_walk.num_points))
	plt.scatter(r_walk.x, r_walk.y, c=point_nums, cmap=plt.cm.Reds, edgecolor='none',  s=20)

	# Emphasize first and last points
	plt.scatter(0, 0, c='blue', edgecolors='none', s=100)
	plt.scatter(r_walk.x[-1], r_walk.y[-1], c='green', edgecolors='none', s=100)
	# Remove the axes
	plt.xticks([])
	plt.yticks([])

	plt.show()
	contin = raw_input("Another walk? (y/n): ")
	if contin == 'n':
		break 
		 