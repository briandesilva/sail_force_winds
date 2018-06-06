
import numpy as np

def get_force(boat,wind,sail):
	"""
	boat is the velocity vector of the boat
	wind is the velocity vector of the wind
	sail is the direction of the sail (should have angle in [pi,2pi])
	"""

	# Function computing the norm of a length 2 vector
	def norm(v):
		return np.sqrt(np.sum(v**2))

	assert sail[1] <= 0 , "Error! sail angle should be between pi and 2pi (its y-component should be negative)."
	assert norm(boat) > 0, "Error! boat cannot be the zero vector!"
	assert norm(sail) > 0, "Error! sail vector cannot be 0!"

	# Compute effective wind
	effective_wind = boat - wind

	# Ensure sail and boat directions is a unit vector
	sail = sail / norm(sail)

	# Pick which side of sail to apply wind force
	sail_perp = np.array([-sail[1],sail[0]])

	ws = np.dot(sail_perp,effective_wind)
	if ws == 0:
		return 0

	if ws < 0:
		sail_perp = -sail_perp

	# Compute resultant force on boat in direction of boat
	force = norm(effective_wind) * np.dot(boat / norm(boat),sail_perp)

	return force


# Test it out
assert(get_force(np.zeros(2),np.zeros(2)))

boat = np.array([0,-1./2])
wind = np.array([0,-1])
sail = np.array([1,0])

print get_force(boat,wind,sail)