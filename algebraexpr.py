from deap import algorithms
from deap import creator
from deap import base
from deap import tools
import random
import numpy
NUMBER_GOAL = 23

#Se evaluan los individuos
def evaluate(individual):
    print(individual)
    val = individual[0]
    for i in range(1, 10, 2):
        if individual[i] == '+':
            val += individual[i + 1]
        elif individual[i] == "-":
            val -= individual[i + 1]
        elif individual[i] == "*":
            val = val * individual[i + 1]
        elif individual[i] == "/":
            val = val / individual[i + 1]
    return (val - NUMBER_GOAL),

#Se generan individuos
def generateIndivual(str):
    ind = list()
    for i in range(0, 11):
        if i%2 == 0:
            number = random.randint(0, 9)
            ind.append(number)
        else:
            operator = random.randint(1, 4)
            if operator == 1:
                ind.append("+")
            elif operator == 2:
                ind.append("-")
            elif operator == 3:
                ind.append("*")
            elif operator == 4:
                ind.append("/")
    return ind

#print(generateIndivual())

creator.create('FitnessMin', base.Fitness, weights=(-1.0, ))
creator.create('Individual', list, fitness = creator.FitnessMin)
toolbox = base.Toolbox()
toolbox.register('individual', generateIndivual, creator.Individual)
ind1 = toolbox.individual()
toolbox.register('population', tools.initRepeat, list, toolbox.individual)
toolbox.register('mate', tools.cxPartialyMatched)
toolbox.register('mutate', tools.mutShuffleIndexes, indpb = 0.2)
toolbox.register('select', tools.selTournament, tournsize = 5)
toolbox.register('evaluate', evaluate)

def main():
    pop = toolbox.population(n = 50)
    print(pop)
    hof = tools.HallOfFame(1)
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", numpy.mean)
    stats.register("std", numpy.std)
    stats.register("min", numpy.min)
    stats.register("max", numpy.max)
    algorithms.eaSimple(pop, toolbox, 0.7, 0.2, 60, stats = stats, halloffame = hof)
    return pop

'''data = generateIndivual(10)
print(data)
print(evaluate(data))'''
print(main())
