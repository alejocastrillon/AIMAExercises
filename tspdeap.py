from deap import algorithms
from deap import creator
from deap import base
from deap import tools
import random
import numpy
import math

cities = [(1290, 345), (234, 4506), (546, 876), (2900, 430), (546, 120), (7600, 900)]

def generateRoute():
    route = numpy.arange(len(cities))
    numpy.random.shuffle(route)
    return route

def validateRoute(route):
    return len(route) == len(set(route))

def regenerateRoute(route):
    final_list= list()
    for x in route:
        if x not in final_list:
            final_list.append(x)
        else:
            y = random.randint(0, len(cities) - 1)
            while y in final_list:
                y = random.randint(0, len(cities) - 1)
            final_list.append(y)
    return final_list

def evaluateRoute(route):
    distancia = 0 
    if validateRoute(route) is False:   
        route = regenerateRoute(route)
    for i in range(len(route) - 1):
        distancia += math.sqrt(math.pow((cities[route[i]][0] - cities[route[i + 1]][0]), 2) + math.pow((cities[route[i]][1] - cities[route[i + 1]][1]), 2))
    distancia += math.sqrt(math.pow((cities[route[len(route) - 1]][0] - cities[route[0]][0]), 2) + math.pow((cities[route[len(route) - 1]][1] - cities[route[0]][1]), 2))
    return distancia, 



creator.create('FitnessMin', base.Fitness, weights = (-1.0, ))
creator.create('Individual', list, fitness = creator.FitnessMin)
toolbox = base.Toolbox()
toolbox.register('individual', tools.initIterate, creator.Individual, generateRoute)
toolbox.register('population', tools.initRepeat, list, toolbox.individual)
toolbox.register('mate', tools.cxOnePoint)
toolbox.register('mutate', tools.mutShuffleIndexes, indpb = 0.2)
toolbox.register('select', tools.selTournament, tournsize = 4)
toolbox.register('evaluate', evaluateRoute)

def main():
    pop = toolbox.population(n = 2000)
    hof = tools.HallOfFame(4)
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", numpy.mean)
    stats.register("std", numpy.std)
    stats.register("min", numpy.min)
    stats.register("max", numpy.max)
    algorithms.eaSimple(pop, toolbox, 0.02, 0.2, 100, stats = stats, halloffame = hof)
    print("Hall of fame: ", hof[0])
    print("Distancia:" , evaluateRoute(hof[0]))

main()