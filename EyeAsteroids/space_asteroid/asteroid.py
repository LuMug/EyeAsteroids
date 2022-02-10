import pygame
from utils import load_sprite

class Asteroid(Game):
	MIN_DISTANCE = 200;

	def __init__:
		super().__init__(
			random_position(), load_sprite("asteroid"), random_velocity()
		)



	def random_position():
		x, y = pygame.display.get_surface().get_size()
		random_x = random.randint(0, x)
		random_y = random.randint(0, y)
		if random_x > x - x/2 - MIN_DISTANCE and random_x < x - x/2 + MIN_DISTANCE:
			if x >= x/2:
				random_x = x/2 + MIN_DISTANCE
			else:
				random_x = x/2 - MIN_DISTANCE
		if random_y > y - y/2 - MIN_DISTANCE and random_y < y - y/2 + MIN_DISTANCE:
			if y >= y/2:
				random_y = y/2 + MIN_DISTANCE
			else:
				random_y = y/2 - MIN_DISTANCE
		return Vector2(random_x, random_y)


	def random_velocity():
		speed = random.randint(20, 60)
		return Vector2(speed)