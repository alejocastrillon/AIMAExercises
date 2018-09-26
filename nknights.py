#!python2

from deap import algorithms
from deap import creator
from deap import base
from deap import tools

import random

# Parametros del Problema
WIDTH = 8
HIGHT = 8

class Knight(object):

	def __init__(self, x=None, y=None):
		self._x = x if x else random.randint(0, WIDTH)
		self._y = y if y else random.randint(0, HIGHT)

	def __hash__(self):
		return 100 * self.x + self.y

	def __repr__(self):
		return '(%r, %r)' % (self.x, self.y)

	def __eq__(self,other):
		return self.x == other.x and self.y == other.y

	@property
	def x(self):
		return self._x
	
	@property
	def y(self):
		return self._y
	
	def attacks(self):
		return [k for k in set(
			Knight(x + self.x, y + self.y)
				for x in [-2, -1, 1, 2] if 0 <= x + self.x < WIDTH
				for y in [-2, -1, 1, 2] if 0 <= y + self.y < HIGHT and abs(y) != abs(x))]


def evalNKnights(individual):
	attacked = set(pos
		for k in individual for pos in k.attacks())
	return len(individual), len(attacked)

creator.create('FitnessMin', base.Fitness, weights=(-1,0, 1.0))
creator.create('Individual', list, fitness=creator.FitnessMin)

toolbox = base.Toolbox()

toolbox.register(
	'individual', 
	tools.initIterate, 
	creator.Individual, 
	toolbox.permutation)
toolbox.register(
	'population', 
	tools.initRepeat, 
	list, 
	toolbox.individual)

toolbox.register('evaluate', evalNKnights)
toolbox.register('mate', tools.cxPartialyMatched)
toolbox.register('mutate', tools.mutShuffleIndexes, indpb=2.0/NB_QUEENS)
toolbox.register('select', tools.selTournament, tournsize=3)