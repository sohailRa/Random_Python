from random import choice

class RandomWalk():
	# Class to generate random walks

	def __init__(self, num_points=5000):

		self.num_points = num_points

		# Initial walks starts at (0,0)
		self.x = [0]
		self.y = [0]


	def walk(self):

		# Keep taking steps until the walk reaches the desired length
		while len(self.x) < self.num_points:
			# Decide direction and how far in that direction
			x_dir = choice([1, -1])
			x_dis = choice([0, 1, 2, 3, 4])
			x_step = x_dir * x_dis

			y_dir = choice([1, -1])
			y_dis = choice([0, 1, 2, 3, 4])
			y_step = y_dir * y_dis

			# Rejecting moves that go nowhere
			if x_step ==0 and y_step == 0:
				continue

			# Next x and y values
			next_x = self.x[-1] + x_step
			next_y = self.y[-1] + y_step

			self.x.append(next_x)
			self.y.append(next_y)

			
