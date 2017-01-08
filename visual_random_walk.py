import matplotlib.pyplot as plt
from random_walk import RandomWalk

r_walk = RandomWalk()
r_walk.walk()

plt.scatter(r_walk.x, r_walk.y, s=20)
plt.show()